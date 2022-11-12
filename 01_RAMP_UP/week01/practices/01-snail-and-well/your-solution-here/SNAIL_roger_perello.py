well_lenght = 125
daily_advance = 30
daily_drop = 20
total_distance = 0
days = 0


while True:
    total_distance = total_distance + daily_advance - daily_drop
    days += 1
    if total_distance >= well_lenght:
        break


print(f"Días = {days}")
