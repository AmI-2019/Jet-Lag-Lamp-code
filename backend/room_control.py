import firebase_admin
from datetime import datetime, date
from time import sleep
from astral import Astral
from pytz import timezone
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("thejetlaglampapp-1-firebase-adminsdk-7oj9c-d795dc3925.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'Users')
users = users_ref.stream()
today = date.today()
astral = Astral()
print(astral.sunrise_utc(today, 45.06301, 7.66003))
mz = timezone("Europe/Rome")
mydate = datetime.astimezone(astral.sunrise_utc(today, 45.06301, 7.66003), mz)

sunrise = datetime.astimezone(astral.sunrise_utc(today, 45.06301, 7.66003), mz)
sunset = datetime.astimezone(astral.sunset_utc(today, 45.06301, 7.66003), mz)
# GPS coordinates to timezone query
# http://api.timezonedb.com/v2.1/get-time-zone?key=DSZOYLMUORVL&format=xml&by=position&lat=64.17752&lng=-51.71046
# http://api.timezonedb.com/v2.1/get-time-zone?key=DSZOYLMUORVL&format=json&by=position&lat=64.17752&lng=-51.71046
print(mydate)
for user in users:
    schedule_ref = db.collection(u'Users/{}/sleep_schedule'.format(user.id))
    print(u'{} stays {} days abroad'.format(user.id, user.to_dict().get('trip_duration')))
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
            # Play white noise
            # Lamps gradually dim until they turn off
            print("HELLO DARKNESS")

        elif day.get('sleep_time') + day.get('sleep_delta')/2 < datetime.now() < day.get('wake_time'):
            # The room must be LIT, open the curtains 20-30 min before the sunset
            # White noise keeps playing
            # Lamps turn on, the become gradually brighter
            # If outside there's daylight
            print("HELLO LIGHT")

        if datetime.now() == day.get('wake_time'):
            # The user must wake up! Play alarm clock tone
            # Stop playing white noise
            # Lights reach the maximum brightness
            print("WAKE UP")

        n += 1

    # Checking current time
    # TODO: define the STATES of the application, like 'the user is sleeping', 'sunset', 'sunrise' etc.

