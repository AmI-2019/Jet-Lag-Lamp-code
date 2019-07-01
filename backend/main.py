from datetime import datetime, date, timedelta, time
from time import sleep
import pygame
from threading import Thread
import time
import tkinter as tk
from tkinter import *
from astral import Astral
from sleep_schedule import init_schedule, set_time_db
from hue import switch_on, switch_off, sun_set, sun_rise, mix_col
from blinders import shut_down, op_en, st_op


time_schedule = init_schedule()

# Declaring the thread for the white noise playback


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

# Time for the demonstration

background_color = 'white'
color = 'blue'


def tick(time1=''):
    clock_frame.config(text=demo_time.strftime('%H:%M:%S'))


root = tk.Tk()
root.title("Time")
clock_frame = tk.Label(root, font='arial 100 bold', bg=background_color, fg=color)
clock_frame.pack(fill='both', expand=1)
root.geometry('700x500')
root.configure(background="lightgreen")

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
    opened_curtains = True
    sunrise_flag = True
    sunset_flag = True
    noise_thread = WhiteNoise()
    my_sleep = datetime.strftime(day.get('sleep_time'), "%d/%m/%Y %H:%M")
    my_wake = datetime.strftime(day.get('wake_time'), "%d/%m/%Y %H:%M")
    print("\nDay {}:".format(n))
    print("Sleep time: {}".format(my_sleep))
    print("Wake time: {}".format(my_wake))
    set_time_db(my_sleep, my_wake)
    while demo_time <= day.get('wake_time'):
        tick()
        # root.mainloop()
        root.update_idletasks()
        root.update()
        if day.get('sleep_time') < demo_time < day.get('wake_time'):
            # The user is sleeping, play white noise if requested
            if activate_noise:
                play_noise()
                activate_noise = False
                print(demo_time)
                print("Beginning of the sleep period. Activating white noise.")

        if day.get('sleep_time') < demo_time < day.get('sleep_time') + day.get('sleep_delta')/2:
            # The room must be DARK
            # Closing the curtains
            if opened_curtains:
                opened_curtains = False
                shut_down()
            # Dimming the lamps until they turn off
            if sunset_flag:
                sunset_flag = False
                print(demo_time)
                print("Dark phase: closing curtains and starting sunset procedure.")
                t = 1
                col = 1
                color = mix_col(col)
                sun_set(t, color)

        elif day.get('sleep_time') + day.get('sleep_delta')/2 < demo_time < day.get('wake_time'):
            # The room must be LIT, open the curtains 20-30 min before the sunset
            # Turn on Philips Hue --> start sunset procedure
            # Opening curtains
            if opened_curtains == False:
                opened_curtains = True
                op_en()
            # Turning on the lamps, they gradually become brighter
            if sunrise_flag:
                sunrise_flag = False
                print(demo_time)
                print("Light phase: opening curtains and starting sunrise procedure.")
                t = 1
                col = 0
                color = mix_col(col)
                sun_rise(t, color)

    # TODO: if outside there's no sun or it's too strong just turn on the lamps

    # Obtaining sunrise and sunset time from the local time zone
    # today = date.today()
    # astral = Astral()
    # sunrise = datetime.astimezone(astral.sunrise_utc(today, float(latitude), float(longitude)), timezone(arr_zone))
    # sunset = datetime.astimezone(astral.sunset_utc(today, float(latitude), float(longitude)), timezone(arr_zone))
    # print("Sunrise: " + str(sunrise))
    # print("Sunset: " + str(sunset))

        if demo_time >= day.get('wake_time'):
            # The user must wake up! Play alarm clock tone
            print(demo_time)
            print("End of the sleep period. Stopping white noise. Playing alarm clock tone.")
            stop_noise()

        sleep(0.001)
        demo_time += timedelta(seconds=5)
    n += 1
    sleep(2)

