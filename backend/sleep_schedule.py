from datetime import datetime, timedelta
from firebase_admin import credentials
from firebase_admin import firestore
from pytz import timezone
import firebase_admin
import urllib
import xmltodict

# Each datetime is defined as a string as "DD/MM/YYYY HH:MM"

# The function init_schedule() initializes the database, read all the useful data to carry out the computation and
# returns a list of dictionaries containing {sleep time, wake up time, sleep amount}. The first two variables are of
# type datetime, while the third is a timedelta.


def init_schedule():
    # Initializing the connection to Cloud Firestore
    cred = credentials.Certificate("thejetlaglampapp-1-firebase-adminsdk-7oj9c-d795dc3925.json")
    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    fabio_ref = db.document(u'Users/fabio.baldo17@gmail.com')
    schedule_ref = db.collection(u'Users/fabio.baldo17@gmail.com/sleep_schedule')
    fabio = fabio_ref.get()
    fabio_dict = fabio.to_dict()
    events_list = []

    # Deleting previous sleeping time schedule
    n = 0
    for schedule in schedule_ref.stream():
        schedule_ref.document(u'day_{}'.format(str(n).zfill(2))).delete()
        n += 1

    # Retrieving arrival location from db and getting corresponding time zone
    hotel_coord = fabio_dict.get('hotel_address')
    latitude = hotel_coord.split(", ")[0]
    longitude = hotel_coord.split(", ")[1]
    file = urllib.request.urlopen("http://api.timezonedb.com/v2.1/get-time-zone?key=DSZOYLMUORVL&format=xml&by=position&lat={}&lng={}".format(latitude, longitude))
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    arr_zone = data['result']['zoneName']
    dep_zone = fabio_dict.get('dep_zone')

    # Retrieving parameters for sleeping schedule computation
    arr_date = datetime.strptime(fabio_dict.get('arr_date'), "%d/%m/%Y")
    home_sleep_time = datetime.strptime(fabio_dict.get('typicalBedTime'), "%H:%M")
    home_wake_time = datetime.strptime(fabio_dict.get('typicalWakeUpTime'), "%H:%M")
    home_sleep_time = datetime.combine(arr_date - timedelta(days=1), home_sleep_time.time())
    home_wake_time = datetime.combine(arr_date - timedelta(days=1), home_wake_time.time())
    if home_wake_time < home_sleep_time:
        home_wake_time += timedelta(days=1)
    home_sleep_time = datetime.strftime(home_sleep_time, "%d/%m/%Y %H:%M")
    home_wake_time = datetime.strftime(home_wake_time, "%d/%m/%Y %H:%M")
    trip_duration = int(fabio.to_dict().get('trip_duration'))

    # Calling the function that computes the sleeping schedule
    time_schedule = set_schedule(dep_zone, arr_zone, home_sleep_time, home_wake_time, events_list, trip_duration)

    # Writing the sleeping time schedule on the database
    n = 0
    for schedule in time_schedule:
        schedule_ref.document(u'day_{}'.format(str(n).zfill(2))).set(schedule)
        n += 1
    return time_schedule


def set_schedule(dep_place, arr_place, home_sleep_time, home_wake_time, events_list, days):

    # Defining home and local time zones
    dep_zone = timezone(dep_place)
    arr_zone = timezone(arr_place)

    # Defining the sleeping time and the wake up time
    dep_sleep_time = datetime.strptime(home_sleep_time, "%d/%m/%Y %H:%M")
    dep_sleep_time = dep_zone.localize(dep_sleep_time)
    dep_wake_time = datetime.strptime(home_wake_time, "%d/%m/%Y %H:%M")
    dep_wake_time = dep_zone.localize(dep_wake_time)
    local_sleep_time = datetime.astimezone(dep_sleep_time, arr_zone)
    local_wake_time = datetime.astimezone(dep_wake_time, arr_zone)

    # Other parameters and work variables
    time_list = []

    # Difference between the time zones
    diff_zone = datetime.utcoffset(local_sleep_time) - datetime.utcoffset(dep_sleep_time)
    if diff_zone > timedelta(days=0, hours=0, minutes=0):
        direction = 'east'
    else:
        direction = 'west'

    diff_zone = abs(diff_zone)

    # Inserting the day 0 in the list: the user is still at home
    time_list.append({"sleep_time": dep_sleep_time.strftime("%d/%m/%Y %H:%M"),
                      "wake_time": dep_wake_time.strftime("%d/%m/%Y %H:%M")})

    # Computing the sleeping time schedule
    i = 0
    while i < days:

        # Controlling the travel direction
        if direction == 'east':
            local_sleep_time = local_sleep_time - diff_zone/days
            local_wake_time = local_wake_time - diff_zone/days

        elif direction == 'west':
            local_sleep_time = local_sleep_time + diff_zone/days
            local_wake_time = local_wake_time + diff_zone/days

        wake_time = local_wake_time
        sleep_time = local_sleep_time

        # Adapting the schedule to the appointments of the user
        for x in events_list:
            start_time = datetime.strptime(x["start_time"], "%d/%m/%Y %H:%M")
            start_time = arr_zone.localize(start_time)
            if sleep_time < start_time < wake_time:
                # Start the procedure for anticipating the alarm clock
                # Set the alarm 1 hour before the beginning of the event
                local_wake_time = start_time - timedelta(hours=1)
                local_sleep_time = local_wake_time - timedelta(hours=7)
                # mySleep = myWake - (dep_wake_time - dep_sleep_time)
                break

        # Writing the list with the sleeping schedule
        time_list.append({"sleep_time": local_sleep_time.strftime("%d/%m/%Y %H:%M"),
                          "wake_time": local_wake_time.strftime("%d/%m/%Y %H:%M")})
        local_sleep_time = local_sleep_time + timedelta(days=1)
        local_wake_time = local_wake_time + timedelta(days=1)
        i += 1

    return time_list
