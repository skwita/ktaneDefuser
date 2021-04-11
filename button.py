from tkinter import *


class MyButton:
    def __init__(self, master, num_battery, ind_car, ind_frk):
        self.top = Toplevel(master)
        self.top.title('Кнопка')
        self.top.geometry('500x400+300+250')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)

        self.num_battery = num_battery.get()
        self.ind_car = ind_car.get()
        self.ind_frk = ind_frk.get()

        self.title = {
            'Abort',
            'Detonate'
            'Hold'
            'Press'
        }

        # Кнопки
        self.red = Button(self.top, bg="#f55353", width=10, height=2,)
        self.red.pack(side=LEFT)

        self.blue = Button(self.top, bg="#5653f5", width=10, height=2,)
        self.blue.pack(side=LEFT)

        self.yellow = Button(self.top, bg="#d4f553", width=10, height=2,)
        self.yellow.pack(side=LEFT)

        self.black = Button(self.top, bg="#fff", width=10, height=2,)
        self.black.pack(side=LEFT)

        self.white = Button(self.top, bg="#fff", width=10, height=2,)
        self.white.pack(side=LEFT)


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    num = IntVar(5)
    window = MyButton(root, num, False, True)
    root.mainloop()
