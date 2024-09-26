import sqlite3

# Ma'lumotlar bazasiga ulanish
connection = sqlite3.connect('startup_loyiha.db')
cursor = connection.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS startup(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        phone_number VARCHAR(13) NOT NULL,
        field TEXT NOT NULL,
        startup_loyiha TEXT NOT NULL)""")
    connection.commit()

def insert_database(full_name, phone_number, field, startup_loyiha):
    cursor.execute("""INSERT INTO startup(full_name, phone_number, field, startup_loyiha) 
        VALUES (?, ?, ?, ?)""", (full_name, phone_number, field, startup_loyiha))
    connection.commit()

def get_startup(connection):
    cursor = connection.cursor()
    return cursor.execute('SELECT * FROM startup').fetchall()

def delete_startup(k):
    cursor.execute('DELETE FROM startup WHERE id=?', (k,))
    connection.commit()

def update_startup(full_name, id):
    cursor.execute('UPDATE startup SET full_name=? WHERE id=?', (full_name, id))
    connection.commit()

def choose_startup(p):
    cursor = connection.cursor()
    return cursor.execute('SELECT * FROM startup WHERE id=?', (p,)).fetchone()

# Funksiyalarni chaqirish
# create_table()  # Agar kerak bo'lsa, jadvalni yaratish uchun faollashtiring
# insert_database('ASILBEK', '+998908968807', 'DASTURCHI', 'BOT YARATISH')
# update_startup('YANGI_ISM', 30)
# print(get_startup(connection))  # connection argumentini bering
# connection.close()
