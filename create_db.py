import sqlite3
con = sqlite3.connect("energy_bill.db")

cur = con.cursor()

cur.execute("""
    CREATE TABLE energy_bill(
        id INTEGER PRIMARY KEY,
        day_reading REAL,
        night_reading REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
""")