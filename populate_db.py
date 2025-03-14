import sqlite3
con = sqlite3.connect("energy_bill.db")

cur = con.cursor()

cur.execute("""
    INSERT INTO energy_bill (day_reading, night_reading, timestamp) VALUES
        (10340, 5993, '2025-01-09 12:00:00'),
        (10370, 6028, '2025-01-10 12:00:00'),
        (10406, 6067, '2025-01-11 12:00:00'),
        (10442, 6104, '2025-01-12 12:00:00'),
        (10467, 6139, '2025-01-13 12:00:00'),
        (10479, 6149, '2025-01-14 12:00:00'),
        (10499, 6158, '2025-01-15 12:00:00'),   
        (10511, 6181, '2025-01-16 12:00:00'),
        (10526, 6213, '2025-01-17 12:00:00'),
        (10545, 6245, '2025-01-18 12:00:00'),
        (10572, 6275, '2025-01-19 12:00:00'),
        (10586, 6307, '2025-01-20 12:14:00'),
        (10597, 6338, '2025-01-21 10:42:00'),
        (10613, 6372, '2025-01-22 12:17:00'),
        (10633, 6406, '2025-01-23 12:34:00'),    
        (10650, 6439.5, '2025-01-24 12:34:00'),
        (10711, 6538, '2025-01-24 12:24:00'),
        (10667, 6473, '2025-01-25 12:34:00'),
        (10686.8, 6504, '2025-01-26 12:00:00'),
        (10706.6, 6535, '2025-01-27 12:00:00'),
        (10726.4, 6566, '2025-01-28 12:00:00'),
        (10746.2, 6597, '2025-01-29 12:00:00'),
        (10766, 6628, '2025-01-30 10:38:00'),
        (10784, 6657, '2025-01-31 11:17:00'),
        (11442, 7777, '2025-03-10 15:54:00')
""")    

con.commit()