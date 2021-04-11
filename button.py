from tkinter import *


class MyButton:
    def __init__(self, master, num_battery, ind_car, ind_frk):
        self.top = Toplevel(master)
        self.top.title('Кнопка')
        self.top.geometry('500x400+300+250')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)

        self.num_battery = int(num_battery.get())
        self.ind_car = bool(ind_car.get())
        self.ind_frk = bool(ind_frk.get())

        self.title = {
            'Abort',
            'Detonate'
            'Hold'
            'Press'
        }

