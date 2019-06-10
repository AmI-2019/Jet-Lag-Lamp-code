import firebase_admin
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
        wake_time = schedule.to_dict().get('wake_time')
        sleep_time = schedule.to_dict().get('sleep_time')
        print("Sleep time: {}".format(sleep_time))
        print("Wake time: {}".format(wake_time))

    # Checking current time

