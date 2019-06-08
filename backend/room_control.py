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

    dep_zone = user.to_dict().get('dep_zone')
    arr_zone = user.to_dict().get('arr_zone')
    trip_duration = int(user.to_dict().get('trip_duration'))
    time_schedule = set_schedule(dep_zone, arr_zone, trip_duration)
    n = 0
    for schedule in time_schedule:
        schedule_ref.document(u'day_{}'.format(n)).set(schedule)
        n += 1
