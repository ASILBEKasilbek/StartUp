import sqlite3
connection=sqlite3.connect('startup_loyiha.db')
cursor=connection.cursor()
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS startup(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        phone_number VARCHART(13) NOT NULL,
        field TEXT NOT NULL,
        startup_loyiha TEXT NOT NULL)""")
    connection.commit()

def insert_database(full_name,phone_number,field,startup_loyiha):
    cursor.execute("""INSERT INTO startup(full_name,phone_number,field,startup_loyiha) 
        VALUES (?,?,?,?)""", (full_name,phone_number,field,startup_loyiha))
    connection.commit()
def get_startup():
    return cursor.execute('SELECT * FROM startup').fetchall()
def delete_startup(k):
    q=cursor.execute('DELETE FROM startup where id=?',(k))
    connection.commit()
    return q
def update_startup(full_name,id):
    w=cursor.execute('UPDATE startup SET age=? WHERE id=?',(full_name,id))
    connection.commit()
    return w

def choose_startup(p):
    return cursor.execute('SELECT * FROM startup WHERE id=?',(p,)).fetchone()
create_table()
#insert_database('ASILBEK','+998908968807','DASTURCHI','BOT YARATISH')
#update_startup(30,8)
#print(get_startup())
connection.close()