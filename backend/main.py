import firebase_admin
from datetime import datetime, date
from time import sleep
from astral import Astral
from pytz import timezone
from sleep_schedule import set_schedule
from firebase_admin import credentials
from firebase_admin import firestore
from play_whitenoise import play_noise
from play_whitenoise import stop_noise


print("I hope you'll like some BROWN NOISE")
play_noise()

cred = credentials.Certificate("thejetlaglampapp-1-firebase-adminsdk-7oj9c-d795dc3925.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()
events_list = []

fabio_ref = db.document(u'Users/fabio.baldo17@gmail.com')
schedule_ref = db.collection(u'Users/fabio.baldo17@gmail.com/sleep_schedule')
fabio = fabio_ref.get()
fabio_dict = fabio.to_dict()
n = 0
for schedule in schedule_ref.stream():
    schedule_ref.document(u'day_{}'.format(str(n).zfill(3))).delete()
    n += 1

hotel_address = fabio_dict.get('hotel_address')
print(hotel_address)

today = date.today()
astral = Astral()
print(astral.sunrise_utc(today, 45.06301, 7.66003))
mz = timezone("Europe/Rome")
mydate = datetime.astimezone(astral.sunrise_utc(today, 45.06301, 7.66003), mz)

sunrise = datetime.astimezone(astral.sunrise_utc(today, 45.06301, 7.66003), mz)
sunset = datetime.astimezone(astral.sunset_utc(today, 45.06301, 7.66003), mz)

print(u'Fabio is staying {} days abroad'.format(fabio_dict.get('trip_duration')))
# home_sleep_time = user_dict.get('home_sleep_time')
# home_wake_time = user_dict.get('home_wake_time')
home_sleep_time = "07/06/2019 23:45"
home_wake_time = "08/06/2019 08:30"
dep_zone = fabio_dict.get('dep_zone')
arr_zone = fabio_dict.get('arr_zone')
trip_duration = int(fabio.to_dict().get('trip_duration'))

time_schedule = set_schedule(dep_zone, arr_zone, home_sleep_time, home_wake_time, events_list, trip_duration)

n = 0
for schedule in time_schedule:
    schedule_ref.document(u'day_{}'.format(str(n).zfill(3))).set(schedule)
    n += 1

print(u'Fabio stays {} days abroad'.format(fabio_dict.get('trip_duration')))
time_schedule = schedule_ref.stream()
my_schedule = []
for schedule in time_schedule:
    wake_time = datetime.strptime(schedule.to_dict().get('wake_time'), "%d/%m/%Y %H:%M")
    sleep_time = datetime.strptime(schedule.to_dict().get('sleep_time'), "%d/%m/%Y %H:%M")
    sleep_delta = wake_time - sleep_time
    # print("Sleep time: {}".format(sleep_time))
    # print("Wake time: {}".format(wake_time))
    my_schedule.append({'sleep_time': sleep_time, 'wake_time': wake_time, 'sleep_delta': sleep_delta})

n = 0
for day in my_schedule:
    print("\nDay {}:".format(n))
    print("Sleep time: {}".format(datetime.strftime(day.get('sleep_time'), "%d/%m/%Y %H:%M")))
    print("Wake time: {}".format(datetime.strftime(day.get('wake_time'), "%d/%m/%Y %H:%M")))
    if day.get('sleep_time') < datetime.now() < day.get('wake_time'):
        # The user is sleeping, play white noise if requested
        print("HELLO!!!")
        sleep(1)

    if day.get('sleep_time') < datetime.now() < day.get('sleep_time') + day.get('sleep_delta')/2:
        # The room must be DARK
        print("HELLO DARKNESS")

    elif day.get('sleep_time') + day.get('sleep_delta')/2 < datetime.now() < day.get('wake_time'):
        # The room must be LIT, open the curtains 20-30 min before the sunset
        print("HELLO LIGHT")

    if datetime.now() == day.get('wake_time'):
        # The user must wake up! Play alarm clock tone
        print("WAKE UP")

    n += 1

# Checking current time
# TODO: define the STATES of the application, like 'the user is sleeping', 'sunset', 'sunrise' etc.
stop_noise()