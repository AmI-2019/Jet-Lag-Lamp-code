import vlc
import time
import threading


class myThreadPlayVLC(threading.Thread):
    def __init__(self, playingTime):
        threading.Thread.__init__(self)
        self.playingTime = playingTime
        playVLC(self.playingTime)


def playVLC(playingtime):
<<<<<<< HEAD
    player = vlc.MediaPlayer("/whiteonoise.wav")
=======
    player = vlc.MediaPlayer("/whitenoise.wma")
>>>>>>> 209bc17f90734a728f923f615d7d5f108a485bce
    player.play()
    time.sleep(playingtime)


if __name__ == '__main__':
    # Create new threads
    thread1 = myThreadPlayVLC(200)

    # Start new Threads
    thread1.start()
