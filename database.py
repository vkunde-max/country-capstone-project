import sqlite3


class CountryDatabaseManager:

    def __init__(self, db_name="countries.db"):
        self.conn = sqlite3.connect(
    db_name,
    check_same_thread=False
)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            name TEXT PRIMARY KEY,
            capital TEXT,
            population INTEGER,
            area REAL
        )
        """)

        self.conn.commit()

    def insert_country(self, country):

        self.cursor.execute("""
        INSERT OR REPLACE INTO countries
        VALUES (?, ?, ?, ?)
        """, (
            country["name"],
            country["capital"],
            country["population"],
            country["area"]
        ))

        self.conn.commit()
    def get_all_countries(self):
        self.cursor.execute("SELECT * FROM countries")
        return self.cursor.fetchall()

    def get_country(self, name):
        self.cursor.execute(
            "SELECT * FROM countries WHERE name=?",
            (name,)
        )
        return self.cursor.fetchone()