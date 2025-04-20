import psycopg2

DB_NAME = "Phonebook"
DB_USER = "postgres"
DB_PASS = "qwert123"
DB_HOST = "localhost"

def connect():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

def create_table_and_procedures():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            phone VARCHAR(15)
        );
    """)

    cur.execute("""
        CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
        RETURNS TABLE(id INT, username TEXT, phone TEXT)
        AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook
            WHERE username ILIKE '%' || pattern || '%'
               OR phone ILIKE '%' || pattern || '%';
        END;
        $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
        CREATE OR REPLACE PROCEDURE insert_or_update_user(uname TEXT, uphone TEXT)
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM phonebook WHERE username = uname) THEN
                UPDATE phonebook SET phone = uphone WHERE username = uname;
            ELSE
                INSERT INTO phonebook (username, phone) VALUES (uname, uphone);
            END IF;
        END;
        $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
        CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[], OUT invalid_data TEXT)
        AS $$
        DECLARE
            i INT := 1;
        BEGIN
            invalid_data := '';
            WHILE i <= array_length(names, 1) LOOP
                IF phones[i] ~ '^\\+?\\d{10,15}$' THEN
                    CALL insert_or_update_user(names[i], phones[i]);
                ELSE
                    invalid_data := invalid_data || format('(%s, %s) ', names[i], phones[i]);
                END IF;
                i := i + 1;
            END LOOP;
        END;
        $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
        CREATE OR REPLACE FUNCTION get_phonebook_page(limit_num INT, offset_num INT)
        RETURNS TABLE(id INT, username TEXT, phone TEXT)
        AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook
            ORDER BY id
            LIMIT limit_num OFFSET offset_num;
        END;
        $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
        CREATE OR REPLACE PROCEDURE delete_by_field(field_name TEXT, field_value TEXT)
        AS $$
        BEGIN
            EXECUTE format('DELETE FROM phonebook WHERE %I = $1', field_name) USING field_value;
        END;
        $$ LANGUAGE plpgsql;
    """)


    conn.commit()
    cur.close()
    conn.close()
    print("Table created successfully.")

def search_by_pattern(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.callproc('search_by_pattern', (pattern,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def insert_or_update_user(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()


def insert_many_users(names, phones):
    conn = connect()
    cur = conn.cursor()
    cur.callproc('insert_many_users', (names, phones))
    result = cur.fetchone()
    print("Invalid entries:", result[0])
    conn.commit()
    cur.close()
    conn.close()

def get_phonebook_page(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.callproc('get_phonebook_page', (limit, offset))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def delete_by_field(field, value):
    conn = connect()
    cur = conn.cursor()
    cur.callproc('delete_by_field', (field, value))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    create_table_and_procedures()

    insert_or_update_user("alice", "+77001234567")
    # insert_or_update_user("bob", "+77007654321")

    # insert_many_users(["john", "jane", "baduser"], ["+1234567890", "not_a_number", "+9988776655"])

    # search_by_pattern("77")
    # get_phonebook_page(5, 0)
    # delete_by_field("username", "bob")