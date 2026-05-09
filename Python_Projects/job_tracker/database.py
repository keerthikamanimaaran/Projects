import sqlite3

def connect():
    return sqlite3.connect("jobs.db")

def create_table():
    conn=connect()

    cursor=conn.cursor()

    cursor.execute("""
    create table if not exists applications(
        id integer primary key autoincrement,
        company text,
        role text,
        status text,
        applied_date date,
        notes text 
    )
    """)
    conn.commit()
    conn.close()