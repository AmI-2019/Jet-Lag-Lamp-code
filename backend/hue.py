import requests
import time

"""
# basic code !!!!!
if __name__ == '__main__':

    # the base URL
    base_url = 'http://192.168.0.201'
    # if you are using the emulator, probably the base_url will be:
    # base_url = 'http://localhost:8000'    #use with the emulator

    # example username, generated by following https://developers.meethue.com/develop/get-started-2/
    username = "-yBmYpKxa2bMpOgle8ZOFBodBuruXHvvQPagKHQI"
    # if you are using the emulator, the username is:
    # username = 'newdeveloper'      #use with the emulator

    # lights URL
    lights_url = base_url + '/api/' + username + '/lights/'

    # get the Hue lights (as JSON)
    all_the_lights = requests.get(lights_url).json()

    if type(all_the_lights) is dict:
        # iterate over the Hue lights, turn them on with the color loop effect
        for light in all_the_lights:
            url_to_call = lights_url + light + '/state'
            # body = {'on': True, 'effect': 'colorloop'}
            # to set the red color
            body = {'on': True, "hue": 0}
            # more colors: https://www.developers.meethue.com/documentation/core-concepts
            requests.put(url_to_call, json=body)

        # wait 10 seconds...
        for i in range(0, 10):
            time.sleep(1)
            print(10 - i)

        # iterate over the Hue lights and turn them off
        for light in all_the_lights:
            url_to_call = lights_url + light + '/state'
            body = {'on': False}
            requests.put(url_to_call, json=body)
    else:
        print('Error:', all_the_lights[0]['error'])
"""


def switch_on(color, intensity):
    # the base URL
    base_url = 'http://192.168.0.201'
    # if you are using the emulator, probably the base_url will be:
    # base_url = 'http://localhost:8000'      # use with the emulator

    # example username, generated by following https://developers.meethue.com/develop/get-started-2/
    username = "-yBmYpKxa2bMpOgle8ZOFBodBuruXHvvQPagKHQI"
    # if you are using the emulator, the username is:
    # username = 'newdeveloper'       # use with the emulator
    light = "3"  # number of the light we are using
    # lights URL
    lights_url = base_url + '/api/' + username + '/lights/'

    # get the Hue lights (as JSON)
    all_the_lights = requests.get(lights_url).json()
    if type(all_the_lights) is dict:
        # iterate over the Hue lights, turn them on with the color loop effect
        for light in all_the_lights:        # activate this loop to switch all lights
            url_to_call = lights_url + light + '/state'
            #body = {'on': True, 'effect': 'colorloop'}
            # to set the red color
            # body = {'on': True, "hue": color, "bri": intensity}
            body = {'on': True, "xy": color, "bri": intensity}
            # more colors: https://www.developers.meethue.com/documentation/core-concepts
        # body = {'on': True, 'effect': 'colorloop'}
        # to set the red color
            #body = {'on': True, "hue": color, "bri": intensity}
            # body = {'on': True, "xy": color, "bri": intensity}
        # more colors: https://www.developers.meethue.com/documentation/core-concepts
            requests.put(url_to_call, json=body)
    else:
        print('Error:', all_the_lights[0]['error'])


def switch_off():
    # the base URL
    base_url = 'http://192.168.0.201'
    # if you are using the emulator, probably the base_url will be:
    # base_url = 'http://localhost:8000'    # use with the emulator

    # example username, generated by following https://developers.meethue.com/develop/get-started-2/
    username = "-yBmYpKxa2bMpOgle8ZOFBodBuruXHvvQPagKHQI"
    # if you are using the emulator, the username is:
    # username = 'newdeveloper'      # use with the emulator
    # light = "12"
    # lights URL
    lights_url = base_url + '/api/' + username + '/lights/'

    # get the Hue lights (as JSON)
    all_the_lights = requests.get(lights_url).json()
    for light in all_the_lights:
        url_to_call = lights_url + light + '/state'
        body = {'on': False}
        requests.put(url_to_call, json=body)


def sun_set(t, color):
    print("Starting the sunset procedure (40s)")
    # the base URL
    base_url = 'http://192.168.0.201'
    # if you are using the emulator, probably the base_url will be:
    # base_url = 'http://localhost:8000'      # use with the emulator

    # example username, generated by following https://developers.meethue.com/develop/get-started-2/
    username = "-yBmYpKxa2bMpOgle8ZOFBodBuruXHvvQPagKHQI"
    # if you are using the emulator, the username is:
    # username = 'newdeveloper'   # use with the emulator

    # lights URL
    lights_url = base_url + '/api/' + username + '/lights/'

    # get the Hue lights (as JSON)
    all_the_lights = requests.get(lights_url).json()
    """
    for i in range(250,1,-50):
        switch_on(color, i)
        # wait 10 seconds...
        for i in range(0, t):
            time.sleep(1)
            print(t - i)
        if i<=50:
            switch_off()
    """
    i = 250

    while i > 50:
        switch_on(color, i)
        # wait 10 seconds...
        for k in range(0, t):
            time.sleep(0.001)
            # print(t - k)
        # i = i - 50
        i -= 10
    switch_off()
    print("Sunset procedure terminated.")


def sun_rise(t, color):
    print("Starting the sunrise procedure (40s)")
    # the base URL
    base_url = 'http://192.168.0.201'
    # if you are using the emulator, probably the base_url will be:
    # base_url = 'http://localhost:8000'  # use with the emulator

    # example username, generated by following https://developers.meethue.com/develop/get-started-2/
    username = "-yBmYpKxa2bMpOgle8ZOFBodBuruXHvvQPagKHQI"
    # if you are using the emulator, the username is:
    # username = 'newdeveloper'       # use with the emulator

    # lights URL
    lights_url = base_url + '/api/' + username + '/lights/'

    # get the Hue lights (as JSON)
    all_the_lights = requests.get(lights_url).json()
    i = 1
    while i < 200:
        switch_on(color, i)
        # wait 10 seconds...
        for k in range(0, t):
            time.sleep(0.001)
            # print(t - k)
        i += 10
        # i = i + 50
    switch_on(color, i)
    """
    for i in range(1,250,50):
        switch_on(color, i)
        # wait 10 seconds...
        for i in range(0, t):
            time.sleep(1)
            print(t - i)
        if i>=200:
            switch_on(color,250)
    """
    print("Sunrise procedure terminated.")


def mix_col(col):
    if col == 1:
        xy = [0.5, 0.4]  # sunrise
        # col = 0
        return xy

    elif col == 0:
        xy = [0.6, 0.35]  # sunset
        # col = 46920
        return xy


# hue : yellow = 25500 / blue=46920 / red= 0/

if __name__ == '__main__':
    col = 0
    color = mix_col(col)
    # color=0
    intensity = 250     # 1 to 254
    t = 10  # 10 seconds: time of waiting
    # colour rouge : 0
    # intensity :50
    # switch_off()
    switch_on(color, intensity)
    # sun_set(t,color)
    """
    switch_off()
    sun_rise(t)
    """
