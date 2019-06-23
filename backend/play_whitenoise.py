import pygame
import time
from threading import Thread

class whitenoise_thread (Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        pygame.mixer.init()
        pygame.mixer.music.load("brownnoise.wav")
        pygame.mixer.music.play(-1)
        while pygame.mixer.music.get_busy() == True:
            continue
        
    def stop(self):
        pygame.mixer.music.fadeout(5000)


thread = whitenoise_thread()
thread.start()
time.sleep(10)
thread.stop()
thread.join()