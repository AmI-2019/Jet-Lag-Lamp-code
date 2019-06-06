import firebase_admin
from sleep_schedule import set_schedule
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("thejetlaglampapp-1-firebase-adminsdk-7oj9c-d795dc3925.json")
default_app = firebase_admin.initialize_app(cred)
schedule = {
    u'sleep_time': u'22:00',
    u'wake_time': u'07:00'
}

db = firestore.client()

users_ref = db.collection(u'Users')
users = users_ref.stream()

for user in users:
    # print(u'{} => {}'.format(user.id, user.to_dict()))
    schedule_ref = db.collection(u'Users/{}/sleep_schedule'.format(user.id))
    print(u'{} stays {} days abroad'.format(user.id, user.to_dict().get('trip_duration')))

    dep_zone = user.to_dict().get('dep_zone')
    arr_zone = user.to_dict().get('arr_zone')
    print(dep_zone, arr_zone)
    trip_duration = int(user.to_dict().get('trip_duration'))
    set_schedule(dep_zone, arr_zone, trip_duration)
    n = 0
    while n < int(user.to_dict().get('trip_duration')):
        schedule_ref.document(u'day_{}'.format(n)).set(schedule)
        n += 1
