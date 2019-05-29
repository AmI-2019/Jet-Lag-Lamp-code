from datetime import datetime, timedelta
from pytz import timezone

# Defining home arrival time zones + UTC
dep_zone = timezone('America/Detroit')
arr_zone = timezone('Europe/Rome')
utc = timezone('UTC')

# Defining the sleeping time and the wake up time
dep_sleep_time = datetime.strptime("23:45", "%H:%M")
dep_sleep_time = dep_zone.localize(dep_sleep_time)
dep_wake_time = datetime.strptime("7:00", "%H:%M")
dep_wake_time = dep_zone.localize(dep_wake_time)
utc_sleep_time = datetime.astimezone(dep_sleep_time, utc)
utc_wake_time = datetime.astimezone(dep_wake_time, utc)
arr_sleep_time = datetime.astimezone(dep_sleep_time, arr_zone)
arr_wake_time = datetime.astimezone(dep_wake_time, arr_zone)

direction = ''

print("Home sleeping time: ", utc_sleep_time.strftime("%H:%M %Z"))
print("Home wake up time: ", utc_wake_time.strftime("%H:%M %Z"))

# Difference between the time zones
diff_zone = datetime.utcoffset(arr_sleep_time) - datetime.utcoffset(dep_sleep_time)
if diff_zone > timedelta(days=0, hours=0, minutes=0):
    direction = 'east'
else:
    direction = 'west'

diff_zone = abs(diff_zone)

# Computing a sleeping schedule without appointments on the calendar
print("Suggested sleeping schedule:")
print("Go to sleep at: ", arr_sleep_time.strftime("%H:%M"))
print("Wake up at: ", arr_wake_time.strftime("%H:%M"))

i = timedelta(days=0, hours=0, minutes=0)

while i < diff_zone:

    if direction == 'east':
        arr_sleep_time = arr_sleep_time - timedelta(hours=1)
        arr_wake_time = arr_wake_time - timedelta(hours=1)
        print("Go to sleep at: ", arr_sleep_time.strftime("%H:%M"))
        print("Wake up at: ", arr_wake_time.strftime("%H:%M"))
        i += timedelta(hours=1)
    elif direction == 'west':
        arr_sleep_time = arr_sleep_time + timedelta(hours=1)
        arr_wake_time = arr_wake_time + timedelta(hours=1)
        print("Go to sleep at: ", arr_sleep_time.strftime("%H:%M"))
        print("Wake up at: ", arr_wake_time.strftime("%H:%M"))
        i += timedelta(hours=1)


# Now it's time to adjust the schedule: read all the appointments
# and set the alarm clock according to them
