import sqlite3


def create_db():

    conn=sqlite3.connect("messages.db")

    cursor=conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages(
    id INTEGER PRIMARY KEY,
    message TEXT
    )
    """)


    conn.commit()
    conn.close()



def save_message(msg):

    conn=sqlite3.connect("messages.db")

    cursor=conn.cursor()


    cursor.execute(
    "INSERT INTO messages(message) VALUES(?)",
    (msg,)
    )


    conn.commit()
    conn.close()
