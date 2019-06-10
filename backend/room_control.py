import firebase_admin
from datetime import datetime, timedelta
from pytz import timezone
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("thejetlaglampapp-1-firebase-adminsdk-7oj9c-d795dc3925.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'Users')
users = users_ref.stream()

for user in users:
    schedule_ref = db.collection(u'Users/{}/sleep_schedule'.format(user.id))
    print(u'{} stays {} days abroad'.format(user.id, user.to_dict().get('trip_duration')))
    time_schedule = schedule_ref.stream()
    my_schedule = []
    for schedule in time_schedule:
        wake_time = datetime.strptime(schedule.to_dict().get('wake_time'), "%d/%m/%Y %H:%M")
        sleep_time = datetime.strptime(schedule.to_dict().get('sleep_time'), "%d/%m/%Y %H:%M")
        # print("Sleep time: {}".format(sleep_time))
        # print("Wake time: {}".format(wake_time))
        my_schedule.append({'sleep_time': sleep_time, 'wake_time': wake_time})
        if sleep_time < datetime.now() < wake_time:
            print("HELLO!!!")
    n = 0
    for day in my_schedule:
        print("\nDay {}:".format(n))
        print("Sleep time: {}".format(datetime.strftime(day.get('sleep_time'), "%d/%m/%Y %H:%M")))
        print("Wake time: {}".format(datetime.strftime(day.get('wake_time'), "%d/%m/%Y %H:%M")))
        n += 1

    # Checking current time
    # TODO: define the STATES of the application, like 'the user is sleeping', 'sunset', 'sunrise' etc.

