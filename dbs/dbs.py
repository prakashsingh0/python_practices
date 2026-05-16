import sqlite3

DB_FILE = "sql_users.db"

conn = sqlite3.connect(DB_FILE)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               first_name TEXT NOT NULL,
               last_name TEXT NOT NULL,
               email TEXT NOT NULL UNIQUE,
               age INTEGER)

""")

users_data = [
    ("john","doe","jogn@gamil.com",20),
    ("chandra","ram","ram@gamil.com",20),
    ("shiv","dev","shiv@gamil.com",20),
    ("prakash","singh","singh@gamil.com",20)
]

for user in users_data:
    print(f'Inserting {user[0]} {user[1]}')
    cursor.execute("INSERT INTO users (first_name,last_name, email,age) VALUES (?,?,?,?)", (user[0],user[1],user[2],user[3]))

conn.commit()

conn.close()