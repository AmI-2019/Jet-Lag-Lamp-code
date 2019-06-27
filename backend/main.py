from datetime import datetime, date, timedelta, time
from time import sleep
import pygame
from threading import Thread
from astral import Astral
from sleep_schedule import init_schedule
from hue import switch_on, switch_off, sun_set, sun_rise, mix_col
from blinders import shut_down,op_en,st_op


time_schedule = init_schedule()


class WhiteNoise(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        pygame.mixer.init()
        pygame.mixer.music.load("brownnoise.wav")
        pygame.mixer.music.play(-1)
        while pygame.mixer.music.get_busy():
            continue

    def stop(self):
        pygame.mixer.music.fadeout(5000)


def play_noise():
    noise_thread.start()


def stop_noise():
    noise_thread.stop()
    noise_thread.join()

# Obtaining sunrise and sunset time from the local time zone
# today = date.today()
# astral = Astral()
# sunrise = datetime.astimezone(astral.sunrise_utc(today, float(latitude), float(longitude)), timezone(arr_zone))
# sunset = datetime.astimezone(astral.sunset_utc(today, float(latitude), float(longitude)), timezone(arr_zone))
# print("Sunrise: " + str(sunrise))
# print("Sunset: " + str(sunset))

# Processing the schedule --> room control


my_schedule = []
switch_on(5000, 254)
for schedule in time_schedule:
    wake_time = datetime.strptime(schedule.get('wake_time'), "%d/%m/%Y %H:%M")
    sleep_time = datetime.strptime(schedule.get('sleep_time'), "%d/%m/%Y %H:%M")
    sleep_delta = wake_time - sleep_time
    my_schedule.append({'sleep_time': sleep_time, 'wake_time': wake_time, 'sleep_delta': sleep_delta})

n = 0
for day in my_schedule:
    demo_time = day.get('sleep_time')
    activate_noise = True
    noise_thread = WhiteNoise()
    print("\nDay {}:".format(n))
    print("Sleep time: {}".format(datetime.strftime(day.get('sleep_time'), "%d/%m/%Y %H:%M")))
    print("Wake time: {}".format(datetime.strftime(day.get('wake_time'), "%d/%m/%Y %H:%M")))
    while demo_time <= day.get('wake_time'):
        if day.get('sleep_time') < demo_time < day.get('wake_time'):
            # The user is sleeping, play white noise if requested
            print("HELLO!!!")
            if activate_noise:
                play_noise()
                activate_noise = False

        if day.get('sleep_time') < demo_time < day.get('sleep_time') + day.get('sleep_delta')/2:
            # The room must be DARK
<<<<<<< HEAD

=======
            shut_down()
            t = 10
            col = 1
            color = mix_col(col)
            sun_set(t, color)
>>>>>>> b7a7ba5882dec3b414877435723023a12b3524e0
            print("HELLO DARKNESS")

        elif day.get('sleep_time') + day.get('sleep_delta')/2 < demo_time < day.get('wake_time'):
            # The room must be LIT, open the curtains 20-30 min before the sunset
<<<<<<< HEAD
            # Turn on Philips Hue --> start sunset procedure
            # use a flag like activate_noise
=======
            op_en()
            t = 10
            col = 0
            color = mix_col(col)
            sun_rise(t, color)
>>>>>>> b7a7ba5882dec3b414877435723023a12b3524e0
            print("HELLO LIGHT")

        if demo_time == day.get('wake_time'):
            # The user must wake up! Play alarm clock tone
            stop_noise()
            print("WAKE UP")

        print(demo_time)
        sleep(0.001)
        demo_time += timedelta(seconds=1)
    n += 1
