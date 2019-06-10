import firebase_admin
from sleep_schedule import set_schedule
from firebase_admin import credentials
from firebase_admin import firestore
# from gpstotz import gpstotz
# lat = 51.50
# lon = 0.12
# timezone = gpstotz.gpsToTimezone(lat, lon)

# events_list = [{"name": "wash the car", "start_time": "10/06/2019 09:00", "end_time": "10/06/2019 09:45"},
#                {"name": "pet the hedgehog", "start_time": "10/06/2019 09:45", "end_time": "10/06/2019 10:00"},
#                {"name": "meeting with Faustus", "start_time": "10/06/2019 11:30", "end_time": "10/06/2019 12:30"},
#                {"name": "go to post office", "start_time": "10/06/2019 15:00", "end_time": "10/06/2019 16:00"},
#                {"name": "dinner with Theresa", "start_time": "10/06/2019 19:15", "end_time": "10/06/2019 21:30"},
#                {"name": "beer with Donald", "start_time": "10/06/2019 23:15", "end_time": "11/06/2019 0:30"}]

cred = credentials.Certificate("thejetlaglampapp-1-firebase-adminsdk-7oj9c-d795dc3925.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'Users')
users = users_ref.stream()

events_list = []
fabio_ref = db.document(u'Users/fabio.baldo17@gmail.com')
fabio = fabio_ref.get()
address = fabio.to_dict().get('hotel_address')
print(address)
for user in users:
    user_dict = user.to_dict()
    # print(u'{} => {}'.format(user.id, user.to_dict()))
    schedule_ref = db.collection(u'Users/{}/sleep_schedule'.format(user.id))
    # events_ref = db.collection(u'Users/{}/events'.format(user.id))
    # events = events_ref.stream()
    # for event in events:
    #     events_list.append(event.to_dict())

    print(u'{} stays {} days abroad'.format(user.id, user_dict.get('trip_duration')))
    # home_sleep_time = user_dict.get('home_sleep_time')
    # home_wake_time = user_dict.get('home_wake_time')
    home_sleep_time = "08/06/2019 00:30"
    home_wake_time = "08/06/2019 08:30"
    dep_zone = user_dict.get('dep_zone')
    arr_zone = user_dict.get('arr_zone')
    trip_duration = int(user.to_dict().get('trip_duration'))

    time_schedule = set_schedule(dep_zone, arr_zone, home_sleep_time, home_wake_time, events_list, trip_duration)

    n = 0
    for schedule in time_schedule:
        schedule_ref.document(u'day_{}'.format(n)).set(schedule)
        n += 1
