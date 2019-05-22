import json
from datetime import datetime
import sleep

if __name__ == "__main__":
    with open("dataset.json", "r") as read_file:
        myDict = json.load(read_file)


if 'session' in myDict:
    for activity in myDict['session']:
        if 'activityType' in activity and activity['activityType'] == 72:

            print(datetime.fromtimestamp(int(activity['startTimeMillis'])/1000))
