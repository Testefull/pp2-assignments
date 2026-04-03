CREATE OR REPLACE PROCEDURE insert_or_update(p_name TEXT, p_phone TEXT) AS $$
BEGIN
    INSERT INTO phonebook (first_name, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (phone) DO UPDATE 
    SET name = EXCLUDED.name;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_contact(p_identifier TEXT) AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE first_name = p_identifier OR phone = p_identifier;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE bulk_insert_procedure(names TEXT[], phones TEXT[]) AS $$
DECLARE
    i INT;
BEGIN

    CREATE TEMP TABLE IF NOT EXISTS bulk_errors (
        first_name TEXT,
        phone TEXT
    ) ON COMMIT DROP;

    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^[0-9]{7,}$' THEN
            INSERT INTO phonebook (name, phone) 
            VALUES (names[i], phones[i])
            ON CONFLICT (phone) DO NOTHING;
        ELSE
            INSERT INTO bulk_errors VALUES (names[i], phones[i]);
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;