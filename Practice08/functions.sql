CREATE OR REPLACE FUNCTION search_by_pattern(pattern text)
RETURNS SETOF phonebook AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE first_name ILIKE '%' || pattern || '%'
    OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS SETOF phonebook AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook 
    ORDER BY id 
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;