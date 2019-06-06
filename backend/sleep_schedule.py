from datetime import datetime, timedelta
from pytz import timezone


def set_schedule(dep_place, arr_place, days):

    myAppointments = [{"name": "wash the car", "start_time": "10/06/2019 09:00", "end_time": "10/06/2019 09:45"},
                      {"name": "pet the hedgehog", "start_time": "10/06/2019 09:45", "end_time": "10/06/2019 10:00"},
                      {"name": "meeting with Faustus", "start_time": "10/06/2019 11:30", "end_time": "10/06/2019 12:30"},
                      {"name": "go to post office", "start_time": "10/06/2019 15:00", "end_time": "10/06/2019 16:00"},
                      {"name": "dinner with Theresa", "start_time": "10/06/2019 19:15", "end_time": "10/06/2019 21:30"},
                      {"name": "beer with Donald", "start_time": "10/06/2019 23:15", "end_time": "11/06/2019 0:30"}]

    # Defining home arrival time zones + UTC
    dep_zone = timezone(dep_place)
    arr_zone = timezone(arr_place)
    utc = timezone('UTC')

    # Defining the sleeping time and the wake up time
    dep_sleep_time = datetime.strptime("08/06/2019 23:45", "%d/%m/%Y %H:%M")
    dep_sleep_time = dep_zone.localize(dep_sleep_time)
    dep_wake_time = datetime.strptime("09/06/2019 7:00", "%d/%m/%Y %H:%M")
    dep_wake_time = dep_zone.localize(dep_wake_time)
    utc_sleep_time = datetime.astimezone(dep_sleep_time, utc)
    utc_wake_time = datetime.astimezone(dep_wake_time, utc)
    arr_sleep_time = datetime.astimezone(dep_sleep_time, arr_zone)
    arr_wake_time = datetime.astimezone(dep_wake_time, arr_zone)

    # Other parameters and work variables
    # days = 7
    direction = ''
    time_list = []

    # print("Home sleeping time: ", utc_sleep_time.strftime("%H:%M %Z"))
    # print("Home wake up time: ", utc_wake_time.strftime("%H:%M %Z"))

    # Difference between the time zones
    diff_zone = datetime.utcoffset(arr_sleep_time) - datetime.utcoffset(dep_sleep_time)
    if diff_zone > timedelta(days=0, hours=0, minutes=0):
        direction = 'east'
    else:
        direction = 'west'

    diff_zone = abs(diff_zone)

    # Computing a sleeping schedule without appointments on the calendar
    # print("Suggested sleeping schedule:")
    # print("Day 0 - Home:")
    # print("Go to sleep at: ", dep_sleep_time.strftime("%H:%M"))
    # print("Wake up at: ", dep_wake_time.strftime("%H:%M"), "\n")
    time_list.append({"sleep_time": dep_sleep_time.strftime("%d/%m/%Y %H:%M"),
                      "wake_time": dep_wake_time.strftime("%d/%m/%Y %H:%M")})

    # i = timedelta(days=0, hours=0, minutes=0)
    i = 0
    c = 1

    # In the list I excluded day 0 (home)
    while i < days:

        if direction == 'east':
            arr_sleep_time = arr_sleep_time - diff_zone/days
            arr_wake_time = arr_wake_time - diff_zone/days
            myWake = arr_wake_time
            mySleep = arr_sleep_time
            for x in myAppointments:
                start_time = datetime.strptime(x["start_time"], "%d/%m/%Y %H:%M")
                start_time = arr_zone.localize(start_time)
                if arr_sleep_time < start_time < arr_wake_time:
                    # Start the procedure for anticipating the alarm clock
                    # Set the alarm 1 hour before the beginning of the event
                    myWake = start_time - timedelta(hours=1)
                    mySleep = myWake - timedelta(hours=7)
                    break

            # print("Day %s:" % c)
            # print("Go to sleep at: ", mySleep.strftime("%d/%m/%Y %H:%M"))
            # print("Wake up at: ", myWake.strftime("%d/%m/%Y %H:%M"), "\n")
            # print("Go to sleep at: ", arr_sleep_time.strftime("%d/%m/%Y %H:%M"))
            # print("Wake up at: ", arr_wake_time.strftime("%d/%m/%Y %H:%M"), "\n")
            time_list.append({"sleep_time": arr_sleep_time.strftime("%d/%m/%Y %H:%M"),
                              "wake:time": arr_wake_time.strftime("%d/%m/%Y %H:%M")})
            arr_sleep_time = arr_sleep_time + timedelta(days=1)
            arr_wake_time = arr_wake_time + timedelta(days=1)
            # i += timedelta(hours=1)
            i += 1
            c += 1
        elif direction == 'west':
            arr_sleep_time = arr_sleep_time + diff_zone/days
            arr_wake_time = arr_wake_time + diff_zone/days
            for x in myAppointments:
                start_time = datetime.strptime(x["start_time"], "%d/%m/%Y %H:%M")
                start_time = arr_zone.localize(start_time)
                # print(start_time)
                if arr_sleep_time < start_time < arr_wake_time:
                    # Start the procedure for anticipating the alarm clock
                    # Set the alarm 1 hour before the beginning of the event
                    arr_wake_time = start_time - timedelta(hours=1)
                    break

            # print("Day %s:" % c)
            # print("Go to sleep at: ", arr_sleep_time.strftime("%d/%m/%Y %H:%M"))
            # print("Wake up at: ", arr_wake_time.strftime("%d/%m/%Y %H:%M"), "\n")
            time_list.append({"sleep_time": arr_sleep_time.strftime("%d/%m/%Y %H:%M"),
                              "wake:time": arr_wake_time.strftime("%d/%m/%Y %H:%M")})
            arr_sleep_time = arr_sleep_time + timedelta(days=1)
            arr_wake_time = arr_wake_time + timedelta(days=1)
            # i += timedelta(days=1)
            i += 1
            c += 1

    # a = 0
    # print('HOME:')
    # for x in time_list:
    #     print(a, x)
    #     a += 1

    return time_list
    # TODO: the function must return a LIST containing dictionaries with sleep_time and wake_time for each day
    # Now it's time to adjust the schedule: read all the appointments
    # and set the alarm clock according to them

    # Maybe it's better to add the date
    # Once I have defined the sleeping hours I can manage the interaction with the room
    # These include: Philips Hue, curtains, audio
