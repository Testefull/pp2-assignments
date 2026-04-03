CREATE OR REPLACE PROCEDURE insert_or_update(p_name TEXT, p_phone TEXT) AS $$
BEGIN
    INSERT INTO phonebook (first_name, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (first_name)
    DO UPDATE
    SET phone = EXCLUDED.phone;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE delete_contact(p_identifier TEXT) AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE first_name = p_identifier OR phone = p_identifier;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE bulk_insert_procedure(names TEXT[], phones TEXT[]) AS $$
BEGIN
    
    CREATE TEMP TABLE IF NOT EXISTS bulk_errors (
        first_name TEXT,
        phone TEXT
    ) ON COMMIT DELETE ROWS; 

    TRUNCATE bulk_errors;

    INSERT INTO phonebook (first_name, phone)
    SELECT n, p
    FROM unnest(names, phones) AS t(n, p)
    WHERE p ~ '^[0-9]{7,}$'
    ON CONFLICT (phone) DO NOTHING;

    INSERT INTO bulk_errors (first_name, phone)
    SELECT n, p
    FROM unnest(names, phones) AS t(n, p)
    WHERE p !~ '^[0-9]{7,}$';
END;
$$ LANGUAGE plpgsql;