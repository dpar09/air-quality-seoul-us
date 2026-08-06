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

def insert_readings(records):
    conn = sqlite3.connect("data/air_quality.db")
    cursor = conn.cursor()

    for record in records:
        cursor.execute(
            "INSERT INTO readings (source, city, pollutant, value, timestamp) VALUES (?, ?, ?, ?, ?)",
            (record["source"], record["city"], record["pollutant"], record["value"], record["timestamp"])
        )


    conn.commit()
    conn.close()

if __name__ == "__main__":
    from extract import get_airnow_data, get_waqi_data
    from transform import transform_airnow, transform_waqi

    create_table()

    raw_airnow = get_airnow_data("06033")
    transformed_airnow = transform_airnow(raw_airnow, "Hartford")
    insert_readings(transformed_airnow)

    raw_waqi = get_waqi_data("seoul")
    transformed_waqi = transform_waqi(raw_waqi, "Seoul")
    insert_readings(transformed_waqi)

    print("Data loaded")