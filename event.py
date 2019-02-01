import random
import time
import pyudev
import threading



class event(threading.Thread):
    def __init__(self, callback,thread3):
        threading.Thread.__init__(self)
        self.callback = callback
        self.running = True
        self.thread3 = thread3
        self.context = pyudev.Context()
        self.monitor = pyudev.Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem='usb')



    def stop(self):
        self.running = False
        print("over")

    def run(self):
        while self.running:
            for device in iter(self.monitor.poll, None):
                if device.action == 'add':
                    p = True
                    color = "green"
                    self.callback("Usb key detected", color)
                    self.thread3.detector1(p)
                elif device.action == 'remove':
                    p = False
                    color = "red"
                    self.callback("No usb key detected", color)
                    self.thread3.detector1(p)
                else:
                    time.sleep(0.1)
                time.sleep(1)
