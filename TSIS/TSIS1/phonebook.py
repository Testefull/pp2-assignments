import psycopg2
import csv
import json
from connect import connection


# 1 CREATION OF TABLE

def create_table():
    with open('schema.sql', 'r') as file:
        code = file.read()

    with connection.cursor() as cur:
        cur.execute(code)
        connection.commit()


    print('[INFO] Schemas were loaded\n')
    print('[INFO] Tables Were Successfully Created\n')


# 2 VALUE INSERTION

def insert_contact(name, email, birth_day, group_id, phones):
    with connection.cursor() as cur:
        cur.execute("""
            INSERT INTO contacts (name, email, birthday, group_id)
            VALUES(%s, %s, %s, %s)
            RETURNING id;
    """, (name, email, birth_day, group_id))
    
        contact_id = cur.fetchone()[0]

        for phone, p_type in phones:
            cur.execute("""
                INSERT INTO phones (contact_id, phone, type)
                VALUES (%s, %s, %s);
            """, (contact_id, phone, p_type))

        connection.commit()


def insert_from_console():
    name = input("Enter name: ")
    email = input("Enter email: ")
    birthday = input("Enter birthday (YYYY-MM-DD): ")
    group_id = int(input("Enter group id: "))

    phones = []
    num = int(input("How many phones you want to add: "))
    for i in range(num):
        phone = input("Enter your phone number: ")
        p_type = input("Type (home/work/mobile): ")
        phones.append((phone, p_type))

    insert_contact(name, email, birthday, group_id, phones)
    print("[INFO] Added Successfully\n")


# 3 CSV FILE INSERTION

def insert_csv():
    with connection.cursor() as cur:

        with open('contacts.csv', 'r') as file:
            data = csv.DictReader(file)

            for row in data:
                name = row['name'].strip()
                email = row['email'].strip() if row['email'] else None
                birth_day = row['birthday'].strip() if row['birthday'] else None
                group_name = row['group']

                cur.execute("SELECT id FROM groups WHERE name = %s", (group_name, ))
                group = cur.fetchone()

                if group:
                    group_id = group[0]
                else:
                    cur.execute("""
                        INSERT INTO groups (name) VALUES (%s) RETURNING id
                    """, group_name)

                    group_id = cur.fetchone()[0]

                cur.execute("""
                    INSERT INTO contacts (name, email, birthday, group_id)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id
                """, (name, email, birth_day, group_id))

                contact_id = cur.fetchone()[0]

                phones = row['phones'].split(';')
                for p in phones:
                    if '-' not in p:
                        continue

                    phone, p_type = p.split('-', 1)

                    phone.strip()
                    p_type.strip().lower()

                    if p_type not in ('home', 'work', 'mobile'):
                        continue

                    cur.execute("""
                        INSERT INTO phones (contact_id, phone, type)
                        VALUES (%s, %s, %s)
                    """, (contact_id, phone, p_type))
            
            connection.commit()
            print("[INFO] CSV file was successfully imported\n")


# 4 DATA SELECTION

def select_all_contacts(choice):
    with connection.cursor() as cur:
        cur.execute(f"""
            SELECT
                c.id, c.name, c.email, c.birthday, g.name,
                STRING_AGG(p.phone || ' (' || p.type || ')', ', ' ORDER BY p.id) AS phones
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            LEFT JOIN phones p ON c.id = p.contact_id
            GROUP BY c.id, c.name, c.email, c.birthday, g.name
            ORDER BY c.{choice}
        """)

        return cur.fetchall()


def print_contacts(contacts):
    if not contacts:
        print("[INFO] No contacts\n")
        return
    
    for c in contacts:
        print(f"[{c[0]}] {c[1]} | {c[2]} | {c[3]} | {c[4]} | {c[5]}\n")


# 5 TABLE UPDATING 

def update_contacts():
    contact_id = int(input("Contact ID: "))
    field = input("What value would you like to change (name/email/birthday): ")
    new_value = input("New value: ")

    with connection.cursor() as cur:
        cur.execute(f"""
            UPDATE contacts SET {field} = %s WHERE id = %s
        """, (new_value, contact_id))

        connection.commit()

    print("[INFO] Contacts table was successfully udpdated\n")


# 6 SEARCH BY PATTERN

def find_by_pattern():
    print("Search by:")
    print("1. Name")
    print("2. Phone")
    print("3. Email")
    print("4. Group")

    choice = int(input("Enter choice options: "))
    pattern = input("Input pattern: ").strip()

    with connection.cursor() as cur:
        agg_select = """
            SELECT
                c.id, c.name, c.email, c.birthday, g.name,
                STRING_AGG(p.phone || ' (' || p.type || ')', ', ' ORDER BY p.id) AS phones
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            LEFT JOIN phones p ON c.id = p.contact_id
        """

        if choice == 1:
            cur.execute(agg_select + """
                WHERE c.name ILIKE %s
                GROUP BY c.id, c.name, c.email, c.birthday, g.name
                ORDER BY c.id
            """, (f"%{pattern}%",))
        
        elif choice == 2:
            cur.execute(agg_select + """
                WHERE c.id IN (
                    SELECT contact_id FROM phones WHERE phone ILIKE %s
                )
                GROUP BY c.id, c.name, c.email, c.birthday, g.name
                ORDER BY c.id
            """, (f"%{pattern}%",))
        
        elif choice == 3:
            cur.execute(agg_select + """
                WHERE c.email ILIKE %s
                GROUP BY c.id, c.name, c.email, c.birthday, g.name
                ORDER BY c.id
            """, (f"%{pattern}%",))
        
        elif choice == 4:
            cur.execute(agg_select + """
                WHERE g.name ILIKE %s
                GROUP BY c.id, c.name, c.email, c.birthday, g.name
                ORDER BY c.id
            """, (f"%{pattern}%",))

        else:
            print("[INFO] Invalid Choice")
            return []

        return cur.fetchall()


# 7 DROPPING TABLE

def drop_table():
    command = """DROP TABLE IF EXISTS phones CASCADE;
                 DROP TABLE IF EXISTS contacts CASCADE;
                 DROP TABLE IF EXISTS groups CASCADE;"""

     
    with connection.cursor() as cur:
        cur.execute(command)
        connection.commit()

# 8 FILTERING BY GROUP

def filter_by_group():
    group = input("Enter group name: ").strip()

    with connection.cursor() as cur:
        cur.execute("""
            SELECT
                c.id, c.name, c.email, c.birthday, g.name,
                STRING_AGG(p.phone || ' (' || p.type || ')', ', ' ORDER BY p.id) AS phones
            FROM contacts c
            JOIN groups g ON c.group_id = g.id
            LEFT JOIN phones p ON c.id = p.contact_id
            WHERE g.name ILIKE %s
            GROUP BY c.id, c.name, c.email, c.birthday, g.name
            ORDER BY c.id
        """, (f"%{group}%",))

        return cur.fetchall()
    

# 9 PAGINATION

def pagination():
    page = 0
    size = 5

    while True:
        offset = page * size

         
        with connection.cursor() as cur:
            cur.execute("""
                SELECT * FROM pagination(%s, %s);
            """, (size, offset))

            rows = cur.fetchall()
        
        if not rows:
            print("[INFO] No more data")
            if page > 0:
                page -= 1
            continue

        print(f"\nPage: {page + 1}")
        print_contacts(rows)

        cmd = input("n-next | p-prev | q-quit: ").lower()

        if cmd == "n":
            page += 1
        elif cmd == "p" and page > 0:
            page -= 1
        elif cmd == "q":
            break


# 10 PROCEDURES

def insert_by_name():
    name = input("Name: ")
    phone = input("Phone: ")

     
    with connection.cursor() as cur:
        cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        connection.commit()
    
    print("[INFO] Upsert was Successfully completed\n")


def insert_many_names():
    names = input("Names: ").split()
    phones = input("Phones: ").split()

    if len(names) != len(phones):
        print("[INFO] Mismatch")
        return
    
     
    with connection.cursor() as cur:
        cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
        connection.commit()

    print("Inserted many\n")



def delete_proc():
    print("Delete contact by:")
    print("- ID (e.g. 5)")
    print("- Name (e.g. Sergey)")
    print("- Email (e.g. test@mail.com)")
    print("- Birthday (YYYY-MM-DD)")
    print("- Phone (e.g. exact phone number)")

    value = input("Enter value: ").strip()

     
    with connection.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM contacts;")
        before = cur.fetchone()[0]

        cur.execute("CALL delete_contact(%s)", (value, ))
        connection.commit()

        cur.execute("SELECT COUNT(*) FROM contacts")
        after = cur.fetchone()[0]


    deleted = before - after

    if deleted > 0:
        print(f"[INFO]Deleted {deleted} contacts\n")
    else:
        print("[INFO]No contacts were deleted\n")


def add_phone_console():
    contact_id = input("Enter contact ID: ").strip()
    
    if not contact_id.isdigit():
        print("[INFO] Invalid ID\n")
        return

    phone = input("Enter phone: ").strip()
    p_type = input("Type (home/work/mobile): ").strip().lower()

     
    with connection.cursor() as cur:
        cur.execute(
            "CALL add_phone(%s, %s, %s)",
            (int(contact_id), phone, p_type)
        )
        connection.commit()

    print("[INFO] Phone Added")


def move_to_group_console():
    contact_id = input("Enter contact ID: ").strip()

    if not contact_id.isdigit():
        print("Invalid ID\n")
        return

    group = input("Enter new group name: ").strip()

     
    with connection.cursor() as cur:
        cur.execute(
            "CALL move_to_group(%s, %s)",
            (int(contact_id), group)
        )
        connection.commit()

    print("[INFO] Contact was added to group updated\n")


# 11 LOAD SQL

with open('functions.sql', 'r') as f:
    with connection.cursor() as cur:
        cur.execute(f.read())
    connection.commit()

with open('procedures.sql', 'r') as d:
    with connection.cursor() as cur:
        cur.execute(d.read())
    connection.commit()


# 12 LOAD TO JSON

def load_to_json():
     
    with connection.cursor() as cur:
        cur.execute("""
            SELECT 
                c.id, c.name, c.email, c.birthday, g.name,
                p.phone, p.type
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            LEFT JOIN phones p ON c.id = p.contact_id
            ORDER BY c.id
        """)

        rows = cur.fetchall()
    
    data = {}

    for r in rows:
        cid = r[0]

        if cid not in data:
            data[cid] = {
                "name": r[1],
                "email": r[2],
                "birthday": str(r[3]) if r[3] else None,
                "group": r[4],
                "phones": []
            }
        
        if r[5]:
            data[cid]["phones"].append({
                "number": r[5],
                "type": r[6]
            })
    
    result = list(data.values())

    with open("contacts.json", "w", encoding='UTF-8') as f:
        json.dump(result, f, indent=4)
    
    print("[INFO] Exported to contacts.json")


# 13 IMPORT FROM JSON

def import_from_json():
    with open('contacts.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)

     
    with connection.cursor() as cur:
        for contact in data:
            name = contact['name']
            email = contact['email']
            birthday = contact['birthday']
            group_name = contact['group']


            cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
            existing = cur.fetchone()

            if existing:
                action = input(f"{name} already exists in table. skip / overwrite: ").lower()

                if action == 'skip':
                    continue

                elif action == 'overwrite':
                    cur.execute("DELETE FROM contacts WHERE id = %s", (existing[0],))

                else:
                    continue

            cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
            group = cur.fetchone()

            if group:
                group_id = group[0]

            else:
                cur.execute(
                    "INSERT INTO groups (name) VALUES (%s) RETURNING id",
                    (group_name,)
                )

                group_id = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO contacts (name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (name, email, birthday, group_id))

            contact_id = cur.fetchone()[0]

            for p in contact["phones"]:
                cur.execute("""
                    INSERT INTO phones (contact_id, phone, type)
                    VALUES (%s, %s, %s)
                """, (contact_id, p["number"], p["type"]))

        connection.commit()
    
    print("[INFO] Imported from JSON")


while True:
    command = int(input("""
1. Create tables
2. Insert from console
3. Insert from csv
4. Update
5. Show contacts
6. Find by pattern
7. Pagination
8. Delete by name|id|phone|birthday|email
9. Add phone
10. Filter by group
11. Export to json
12. Import from json 
13. Move to group
0. Exit

Choose: """))

    if command == 1:
        create_table()

    elif command == 2:
        insert_from_console()

    elif command == 3:
        insert_csv()

    elif command == 4:
        update_contacts()

    elif command == 5:
        choice = input("Order by (id/birthday/email): ")
        print_contacts(select_all_contacts(choice))

    elif command == 6:
        print_contacts(find_by_pattern())

    elif command == 7:
        pagination()

    elif command == 8:
        delete_proc()

    elif command == 9:
        add_phone_console()

    elif command == 10:
        print_contacts(filter_by_group())
    
    elif command == 11:
        load_to_json()
    
    elif command == 12:
        import_from_json()
    
    elif command == 13:
        move_to_group_console()
    

    elif command == 99:
        drop_table()

    elif command == 0:
        break


connection.close()
print("Goodbye!")

