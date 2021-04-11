from tkinter import *


class MyButton:
    def __init__(self, master, num_battery, ind_car, ind_frk):
        self.top = Toplevel(master)
        self.top.title('Кнопка')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)

        self.num_battery = num_battery.get()
        self.ind_car = ind_car.get()
        self.ind_frk = ind_frk.get()

        self.color = ''
        self.title = ''

        self.row1 = Frame(self.top)
        self.red = Button(self.row1, bg="#f55353", width=10, height=2, command=self.set_red)
        self.red.pack(side=LEFT, pady=5, padx=5)
        self.blue = Button(self.row1, bg="#5653f5", width=10, height=2, command=self.set_blue)
        self.blue.pack(side=LEFT, pady=5, padx=5)
        self.yellow = Button(self.row1, bg="#f2f553", width=10, height=2, command=self.set_yellow)
        self.yellow.pack(side=LEFT, pady=5, padx=5)
        self.row1.pack()

        self.row2 = Frame(self.top)
        self.black = Button(self.row2, bg="#000", width=10, height=2, command=self.set_black)
        self.black.pack(side=LEFT, pady=5, padx=15)
        self.white = Button(self.row2, bg="#fff", width=10, height=2, command=self.set_white)
        self.white.pack(side=LEFT, pady=5, padx=15)
        self.row2.pack()

        self.row3 = Frame(self.top)
        self.abort = Button(self.row3, text='Abort', width=10, height=2, command=self.set_abort)
        self.abort.pack(side=LEFT, pady=5, padx=5)
        self.detonate = Button(self.row3, text='Detonate', width=10, height=2, command=self.set_detonate)
        self.detonate.pack(side=LEFT, pady=5, padx=5)
        self.hold = Button(self.row3, text='Hold', width=10, height=2, command=self.set_hold)
        self.hold.pack(side=LEFT, pady=5, padx=5)
        self.press = Button(self.row3, text='Press', width=10, height=2, command=self.set_press)
        self.press.pack(side=LEFT, pady=5, padx=5)
        self.row3.pack()

        self.row4 = Frame(self.top)
        self.btn1 = Button(self.row4, text="Клик!", width=10, height=2, command=self.enter)
        self.btn1.pack(side=LEFT, pady=5, padx=15)
        self.btn2 = Button(self.row4, text="clear", width=10, height=2, command=self.clear)
        self.btn2.pack(side=LEFT, pady=5, padx=15)
        self.row4.pack()

        self.row5 = Frame(self.top)
        self.lbl = Label(self.row5, text="")
        self.lbl.pack(side=LEFT, pady=5, padx=15)
        self.row5.pack()

        self.row6 = Frame(self.top)
        self.rules = Label(self.row6, text='Синяя -  4\n', bg='#5653f5')
        self.rules.pack(side=LEFT, pady=1, padx=15)
        self.row6.pack()

        self.row7 = Frame(self.top)
        self.rules = Label(self.row7, text='Белая - 1\n', bg='#fff')
        self.rules.pack(side=LEFT, pady=1, padx=15)
        self.row7.pack()

        self.row8 = Frame(self.top)
        self.rules = Label(self.row8, text='Жёлтая - 5\n', bg='#f2f553')
        self.rules.pack(side=LEFT, pady=1, padx=15)
        self.row8.pack()

        self.row7 = Frame(self.top)
        self.rules = Label(self.row7, text='Другого - 1\n')
        self.rules.pack(side=LEFT, pady=1, padx=15)
        self.row7.pack()

    def set_red(self):
        self.color = 'red'

    def set_blue(self):
        self.color = 'blue'

    def set_yellow(self):
        self.color = 'yellow'

    def set_black(self):
        self.color = 'black'

    def set_white(self):
        self.color = 'white'

    def set_abort(self):
        self.title = 'abort'

    def set_detonate(self):
        self.title = 'detonate'

    def set_hold(self):
        self.title = 'hold'

    def set_press(self):
        self.title = 'press'

    def enter(self):
        result = ''
        if self.color == 'blue' and self.title == 'abort':
            result += 'Зажми'
        elif self.num_battery > 1 and self.title == 'detonate':
            result += 'Нажми и резко отпусти'
        elif self.color == 'white' and self.ind_car:
            result += 'Зажми'
        elif self.num_battery > 2 and self.ind_frk:
            result += 'Нажми и резко отпусти'
        elif self.color == 'yellow':
            result += 'Зажми'
        elif self.color == 'red' and self.title == 'hold':
            result += 'Нажми и резко отпусти'
        else:
            result += 'Зажми'

        self.lbl.configure(text=result)

    def clear(self):
        self.lbl.configure(text='')
        self.color = ''
        self.title = ''


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    num = IntVar(5)
    window = MyButton(root, num, False, True)
    root.mainloop()
