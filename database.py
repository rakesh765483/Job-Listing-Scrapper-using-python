import sqlite3
import pandas as pd

def create_database():
    conn = sqlite3.connect("jobs.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        location TEXT,
        date_posted TEXT
    )
    """)

    df = pd.read_csv("jobs.csv")

    df.to_sql("jobs", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    print("✅ jobs.db created and data inserted")

if __name__ == "__main__":
    create_database()
