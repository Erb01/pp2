import psycopg2

# Данные для подключения — измени при необходимости
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "qwert123"
DB_HOST = "localhost"

def create_tables():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST
    )
    cur = conn.cursor()

    # Создание таблицы пользователей
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE
        );
    """)

    # Таблица для хранения очков и состояний игры
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            level INTEGER,
            score INTEGER,
            saved_state BYTEA
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Таблицы успешно созданы")

# Запуск создания
create_tables()
