#!/usr/bin/python3
# -*-coding:utf-8 -*

import queue, threading
from tkinter import *
from event import event
from event2 import event2
from selector import selector
from graphics import graphics

Queue = queue.Queue()

master = Tk()

def stop():
    thread1.stop()
    thread2.stop()
    thread3.stop()
    master.destroy()


p = graphics(master, Queue, stop)
thread3 = selector(p.status_callback3)
thread1 = event(p.status_callback,thread3)
thread2 = event2(p.status_callback2,thread3)

try:
    thread1.start()
    thread2.start()
    thread3.start()
    master.mainloop()
except KeyboardInterrupt:
    stop()
