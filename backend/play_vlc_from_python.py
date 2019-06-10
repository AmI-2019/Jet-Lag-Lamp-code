import vlc
import time
import threading


class myThreadPlayVLC(threading.Thread):
    def __init__(self, playingTime):
        threading.Thread.__init__(self)
        self.playingTime = playingTime
        playVLC(self.playingTime)


def playVLC(playingtime):
    player = vlc.MediaPlayer("/home/POLITO/s235527/Desktop/whnoise.mp3")
    player.play()
    time.sleep(playingtime)


if __name__ == '__main__':
    # Create new threads
    thread1 = myThreadPlayVLC(200)

    # Start new Threads
    thread1.start()
