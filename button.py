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
        Button(self.row1, bg="#f55353", width=10, height=2, command=self.set_red).pack(side=LEFT, pady=5, padx=5)
        Button(self.row1, bg="#5653f5", width=10, height=2, command=self.set_blue).pack(side=LEFT, pady=5, padx=5)
        Button(self.row1, bg="#f2f553", width=10, height=2, command=self.set_yellow).pack(side=LEFT, pady=5, padx=5)
        self.row1.pack()

        self.row2 = Frame(self.top)
        Button(self.row2, bg="#000", width=10, height=2, command=self.set_black).pack(side=LEFT, pady=5, padx=15)
        Button(self.row2, bg="#fff", width=10, height=2, command=self.set_white).pack(side=LEFT, pady=5, padx=15)
        self.row2.pack()

        self.row3 = Frame(self.top)
        Button(self.row3, text='Abort', width=10, height=2, command=self.set_abort).pack(side=LEFT, pady=5, padx=5)
        Button(self.row3, text='Detonate', width=10, height=2, command=self.set_detonate).pack(side=LEFT, pady=5, padx=5)
        Button(self.row3, text='Hold', width=10, height=2, command=self.set_hold).pack(side=LEFT, pady=5, padx=5)
        Button(self.row3, text='Press', width=10, height=2, command=self.set_press).pack(side=LEFT, pady=5, padx=5)
        self.row3.pack()

        self.row4 = Frame(self.top)
        Button(self.row4, text="Клик!", width=10, height=2, command=self.enter).pack(side=LEFT, pady=5, padx=15)
        Button(self.row4, text="clear", width=10, height=2, command=self.clear).pack(side=LEFT, pady=5, padx=15)
        self.row4.pack()

        self.row5 = Frame(self.top)
        self.lbl = Label(self.row5, text="")
        self.lbl.pack(side=LEFT, pady=5, padx=15)
        self.row5.pack()

        self.row6 = Frame(self.top)
        Label(self.row6, text='Синяя -  4\n', bg='#5653f5').pack(side=LEFT, pady=1, padx=15)
        self.row6.pack()

        self.row7 = Frame(self.top)
        Label(self.row7, text='Белая - 1\n', bg='#fff').pack(side=LEFT, pady=1, padx=15)
        self.row7.pack()

        self.row8 = Frame(self.top)
        Label(self.row8, text='Жёлтая - 5\n', bg='#f2f553').pack(side=LEFT, pady=1, padx=15)
        self.row8.pack()

        self.row7 = Frame(self.top)
        Label(self.row7, text='Другого - 1\n').pack(side=LEFT, pady=1, padx=15)
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
