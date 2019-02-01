from tkinter import *
from selector import selector


class graphics:
    def __init__(self,master, Queue, stop):
        self.output = StringVar()
        self.output.set("No usb key detected")
        self.output2 = StringVar()
        self.output2.set("No mount detected")
        self.Queue = Queue
        self.window = master
        self.Label = Label(self.window, textvariable=(self.output), fg="red")
        self.Label.grid(column="1",row="1")
        self.Label2 = Label(self.window, textvariable=(self.output2), fg="red")
        self.Label2.grid(column="1", row="3")
        self.List = Listbox(self.window, bg="black", fg="white")
        self.List.grid(column="1", row="2")
        master.protocol("WM_DELETE_WINDOW", stop)


    def status_callback(self, msg, color):
        self.output.set(msg)
        self.Label["fg"] = color

    def status_callback2(self, msg, color):
        self.output2.set(msg)
        self.Label2["fg"] = color

    def status_callback3(self, msg):
        self.List.insert(END,*msg)
