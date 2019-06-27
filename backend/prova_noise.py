from time import sleep
import pygame
from threading import Thread
# from play_whitenoise import play_noise, stop_noise


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
    thread.start()


def stop_noise():
    thread.stop()
    thread.join()


thread = WhiteNoise()
play_noise()
sleep(1)
stop_noise()
thread = WhiteNoise()
play_noise()


