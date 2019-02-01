import random
import time
import threading
import os


class event2(threading.Thread):
    def __init__(self, callback2,thread3):
        threading.Thread.__init__(self)
        self.callback2 = callback2
        self.running = True
        self.thread3 = thread3

    def stop(self):
        self.running = False
        print("over")

    def run(self):
        while self.running:
            path = "/media/telmo/"
            if len(os.listdir(path)) > 0:
                p = True
                color = "green"
                self.callback2("Mount detected", color)
                self.thread3.detector2(p)
            elif len(os.listdir(path)) == 0:
                p = False
                color = "red"
                self.callback2("No Mount detected", color)
                self.thread3.detector2(p)
            time.sleep(0.1)