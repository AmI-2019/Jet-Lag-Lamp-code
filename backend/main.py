from datetime import datetime, date, timedelta
from time import sleep
from astral import Astral
from sleep_schedule import init_schedule
from play_whitenoise import play_noise, stop_noise
from clock_demo import start_clock, stop_clock, demo_time

print("BROWN NOISE OP")
play_noise()

time_schedule = init_schedule()

# Obtaining sunrise and sunset time from the local time zone
# today = date.today()
# astral = Astral()
# sunrise = datetime.astimezone(astral.sunrise_utc(today, float(latitude), float(longitude)), timezone(arr_zone))
# sunset = datetime.astimezone(astral.sunset_utc(today, float(latitude), float(longitude)), timezone(arr_zone))
# print("Sunrise: " + str(sunrise))
# print("Sunset: " + str(sunset))

# Processing the schedule --> room control
my_schedule = []
for schedule in time_schedule:
    wake_time = datetime.strptime(schedule.get('wake_time'), "%d/%m/%Y %H:%M")
    sleep_time = datetime.strptime(schedule.get('sleep_time'), "%d/%m/%Y %H:%M")
    sleep_delta = wake_time - sleep_time
    my_schedule.append({'sleep_time': sleep_time, 'wake_time': wake_time, 'sleep_delta': sleep_delta})

n = 0
print("STARTING FAKE TIME")
start_clock(my_schedule[1].get('wake_time'))
for day in my_schedule:
    print("\nDay {}:".format(n))
    print("Sleep time: {}".format(datetime.strftime(day.get('sleep_time'), "%d/%m/%Y %H:%M")))
    print("Wake time: {}".format(datetime.strftime(day.get('wake_time'), "%d/%m/%Y %H:%M")))
    if day.get('sleep_time') < datetime.now() < day.get('wake_time'):
        # The user is sleeping, play white noise if requested
        print("HELLO!!!")
        play_noise()
        sleep(1)

    if day.get('sleep_time') < datetime.now() < day.get('sleep_time') + day.get('sleep_delta')/2:
        # The room must be DARK
        print("HELLO DARKNESS")

    elif day.get('sleep_time') + day.get('sleep_delta')/2 < datetime.now() < day.get('wake_time'):
        # The room must be LIT, open the curtains 20-30 min before the sunset
        print("HELLO LIGHT")

    if datetime.now() == day.get('wake_time'):
        # The user must wake up! Play alarm clock tone
        stop_noise()
        print("WAKE UP")

    n += 1

# Checking current time
# TODO: define the STATES of the application, like 'the user is sleeping', 'sunset', 'sunrise' etc.
print(demo_time())
sleep(2)
print(demo_time())
stop_clock()
print(demo_time())
stop_noise()