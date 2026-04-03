import csv
from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) UNIQUE NOT NULL
    )
    """)

    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            try:
                cur.execute(
                    "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )
            except Exception as e:
                print("Error inserting:", row, e)

    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Inserted successfully!")
    except Exception as e:
        print("Error:", e)

    cur.close()
    conn.close()

def update_contact():
    choice = input("Update (1) Name or (2) Phone? ")

    conn = connect()
    cur = conn.cursor()

    if choice == '1':
        phone = input("Enter phone of contact: ")
        new_name = input("Enter new name: ")

        cur.execute(
            "UPDATE phonebook SET first_name = %s WHERE phone = %s",
            (new_name, phone)
        )

    elif choice == '2':
        name = input("Enter name of contact: ")
        new_phone = input("Enter new phone: ")

        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE first_name = %s",
            (new_phone, name)
        )

    conn.commit()
    print("Updated!")

    cur.close()
    conn.close()

def query_contacts():
    print("1 - All contacts")
    print("2 - Search by name")
    print("3 - Search by phone prefix")

    choice = input("Choose: ")

    conn = connect()
    cur = conn.cursor()

    if choice == '1':
        cur.execute("SELECT * FROM phonebook")

    elif choice == '2':
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE first_name ILIKE %s",
            ('%' + name + '%',)
        )

    elif choice == '3':
        prefix = input("Enter prefix: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE phone LIKE %s",
            (prefix + '%',)
        )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def delete_contact():
    print("Delete by: 1 - Name, 2 - Phone")
    choice = input("Choose: ")

    conn = connect()
    cur = conn.cursor()

    if choice == '1':
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))

    elif choice == '2':
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

    conn.commit()
    print("Deleted!")

    cur.close()
    conn.close()

def execute_db_logic(query, params=None, is_procedure=False):
    conn = connect()
    cur = conn.cursor()
    try:
        if is_procedure:
            cur.execute(f"CALL {query}", params)
        else:
            cur.execute(f"SELECT * FROM {query}", params)
            results = cur.fetchall()
            return results
        
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def search_by_pattern():
    pattern = input("Input a pattern: ")
    results = execute_db_logic("search_by_pattern(%s)", (str(pattern),))

    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

def query_with_pagination():
    limit, offset = input("Input limit and offset: ").split()

    results = execute_db_logic("get_contacts_paginated(%s, %s)", (int(limit), int(offset)))

    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

def insert_or_update():
    name, phone = input("Input name and phone: ").split()

    execute_db_logic("insert_or_update(%s, %s)", (name, phone), is_procedure=True)

    print("Upserted succesfully")

def bulk_insert():
    print("Input in this format: name1 phone1, name2 phone2")
    contacts = input().split(',')
    names = []
    phones = []

    for contact in contacts:
        names.append(contact.split()[0])
        phones.append(contact.split()[1])

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("CALL bulk_insert_procedure(%s, %s)", (names, phones))

        cur.execute("SELECT first_name, phone FROM bulk_errors;")
        errors = cur.fetchall()
        conn.commit()

        if errors:
            print(f"\n--- {len(errors)} Validation Errors Found ---")
            print(f"{'Name':<20} | {'Invalid Phone':<15}")
            print("-" * 40)
            for name, phone in errors:
                print(f"{name or 'None':<20} | {phone or 'None':<15}")
        else:
            print("\nSuccess! All records processed with no validation errors.")
    
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")

    finally:
        if conn:
            cur.close()
            conn.close()

def delete_by_name_or_phone():
    name_or_phone = input("Input name or phone: ")

    execute_db_logic("delete_contact(%s)", (name_or_phone,), is_procedure=True)

    print("Deleted successfully")

def functions_list():
    print("1 - Search by pattern")
    print("2 - Query with pagination")
    
    choice = input("Choose: ")
    if choice == '1':
        search_by_pattern()
    elif choice == '2':
        query_with_pagination()

def procedures_list():
    print("1 - Insert or update")
    print("2 - Insert from list")
    print("3 - Delete by username of phone")

    choice = input("Choose: ")

    if choice == '1':
        insert_or_update()
    elif choice == '2':
        bulk_insert()
    elif choice == '3':
        delete_by_name_or_phone()

def update_functions():
    conn = connect()
    cur = conn.cursor()

    with open("functions.sql", 'r') as f:
        functions = f.read()

        try:
            cur.execute(functions)
            conn.commit()

            print("Updated successfully")
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
            cur.close()
            conn.close()

def update_procedures():
    conn = connect()
    cur = conn.cursor()

    with open("procedures.sql", 'r') as f:
        functions = f.read()

        try:
            cur.execute(functions)
            conn.commit()

            print("Updated successfully")
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
            cur.close()
            conn.close()

def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Functions list")
        print("7. Procedures list")
        print("8. Update functions")
        print("9. Update procedures")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == '1':
            insert_from_csv('contsacts.csv')
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            query_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            functions_list()
        elif choice == '7':
            procedures_list()
        elif choice == '8':
            update_functions()
        elif choice == '9':
            update_procedures()
        elif choice == '0':
            break


if __name__ == "__main__":
    create_table()
    menu()