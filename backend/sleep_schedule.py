from datetime import datetime, timedelta
from pytz import timezone

# Each datetime is defined as a string as "DD/MM/YYYY HH:MM"


def set_schedule(dep_place, arr_place, home_sleep_time, home_wake_time, events_list, days):

    # Defining home and local time zones + UTC
    dep_zone = timezone(dep_place)
    arr_zone = timezone(arr_place)
    utc = timezone('UTC')

    # Defining the sleeping time and the wake up time
    dep_sleep_time = datetime.strptime(home_sleep_time, "%d/%m/%Y %H:%M")
    dep_sleep_time = dep_zone.localize(dep_sleep_time)
    dep_wake_time = datetime.strptime(home_wake_time, "%d/%m/%Y %H:%M")
    dep_wake_time = dep_zone.localize(dep_wake_time)
    utc_sleep_time = datetime.astimezone(dep_sleep_time, utc)
    utc_wake_time = datetime.astimezone(dep_wake_time, utc)
    local_sleep_time = datetime.astimezone(dep_sleep_time, arr_zone)
    local_wake_time = datetime.astimezone(dep_wake_time, arr_zone)

    # Other parameters and work variables
    # days = 7
    direction = ''
    time_list = []

    # Difference between the time zones
    diff_zone = datetime.utcoffset(local_sleep_time) - datetime.utcoffset(dep_sleep_time)
    if diff_zone > timedelta(days=0, hours=0, minutes=0):
        direction = 'east'
    else:
        direction = 'west'

    diff_zone = abs(diff_zone)

    time_list.append({"sleep_time": dep_sleep_time.strftime("%d/%m/%Y %H:%M"),
                      "wake_time": dep_wake_time.strftime("%d/%m/%Y %H:%M")})
    i = 0

    while i < days:

        if direction == 'east':
            local_sleep_time = local_sleep_time - diff_zone/days
            local_wake_time = local_wake_time - diff_zone/days

        elif direction == 'west':
            local_sleep_time = local_sleep_time + diff_zone/days
            local_wake_time = local_wake_time + diff_zone/days

        wake_time = local_wake_time
        sleep_time = local_sleep_time
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

        time_list.append({"sleep_time": local_sleep_time.strftime("%d/%m/%Y %H:%M"),
                          "wake:time": local_wake_time.strftime("%d/%m/%Y %H:%M")})
        local_sleep_time = local_sleep_time + timedelta(days=1)
        local_wake_time = local_wake_time + timedelta(days=1)
        i += 1
            
    return time_list
