from datetime import datetime, timedelta

import sqlite3
con = sqlite3.connect("energy_bill.db")
cur = con.cursor()

day_rate = 0.2961
night_rate = 0.1251
standing_charge = 0.3945

# calculate how much we have spent
def energy_usage(new_day_reading, new_night_reading):
    res = cur.execute("SELECT day_reading, night_reading, timestamp FROM energy_bill ORDER BY id desc LIMIT 1")
    last_reading = res.fetchone()
    print(last_reading)

    timestamp_dt = datetime.strptime(last_reading[2], "%Y-%m-%d %H:%M:%S")
    yesterday = datetime.now().date() - timedelta(days=1)

    if timestamp_dt.date() == yesterday:
        day_usage = int(new_day_reading) - last_reading[0]
        night_usage = int(new_night_reading) - last_reading[1]
        print(f"Day usage:{day_usage} / Night usage:{night_usage}")

        day_cost = day_usage * day_rate
        night_cost = night_usage * night_rate

        yesterday_cost = day_cost + night_cost
        print(f"Yesterday you spent: {yesterday_cost}GBP")
        return yesterday_cost
    
    else:
       pass

# Calculate daily average
# daily_cost = energy_usage()
def daily_average(daily_cost):
    pass

# Total cost so far this month (including standing charge)

energy_usage(10800, 6700)

new_day_reading = input("Enter day reading:")
new_night_reading = input("Enter night reading:")

# print(f"Yesterday you spent: {daily_cost}GBP")