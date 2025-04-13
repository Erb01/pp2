import psycopg2
import csv

DB_NAME = "Phonebook"
DB_USER = "postgres"
DB_PASS = "qwert123"
DB_HOST = "localhost"

def connect():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            phone VARCHAR(15)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(file_path):
    conn = connect()
    cur = conn.cursor()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    conn = connect()
    cur = conn.cursor()
    username = input("Enter a username: ")
    phone = input("Enter your phonenumber: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()
    cur.close()
    conn.close()

def update_user(username, new_name=None, new_phone=None):
    conn = connect()
    cur = conn.cursor()
    if new_name:
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_name, username))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, username))
    conn.commit()
    cur.close()
    conn.close()

def search_phonebook(filter_by, value):
    conn = connect()
    cur = conn.cursor()
    query = f"SELECT * FROM phonebook WHERE {filter_by} = %s"
    cur.execute(query, (value,))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()

def delete_entry(by_field, value):
    conn = connect()
    cur = conn.cursor()
    query = f"DELETE FROM phonebook WHERE {by_field} = %s"
    cur.execute(query, (value,))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_table()
    insert_from_csv('phonebook.csv')
    insert_from_console()
    # update_user('john', new_name='johnny')
    # search_phonebook('username', 'johnny')
    # delete_entry('username', 'johnny')