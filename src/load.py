import sqlite3

def create_table():
    conn = sqlite3.connect("data/air_quality.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            city TEXT,
            pollutant TEXT,
            value REAL,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Table created")