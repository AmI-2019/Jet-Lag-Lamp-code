from time import sleep
from threading import Thread
from datetime import datetime, timedelta


class TimeDemo(Thread):
    def __init__(self, start_time, clock_on):
        Thread.__init__(self)
        self.my_time = start_time
        self.clock_on = clock_on

    def run(self):
        while self.clock_on:
            sleep(0.001)
            self.my_time += timedelta(seconds=3)

    def set(self, start_time):
        self.my_time = start_time

    def stop(self):
        self.clock_on = False


thread = TimeDemo(datetime.now(), True)


def start_clock(start_time):
    thread.set(start_time)
    thread.start()


def stop_clock():
    thread.stop()
    thread.join()


def demo_time():
    return thread.my_time
