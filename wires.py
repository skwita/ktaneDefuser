from tkinter import *
from tkinter.ttk import Radiobutton


class Wires:
    def __init__(self, master, serial_number_last_digit):
        self.top = Toplevel(master)
        self.top.title('Провода')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)

        # счётчик для проводов каждого цвета
        self.num_colors = {
            'r': 0,
            'b': 0,
            'y': 0,
            'k': 0,
            'w': 0
        }

        # инициализация переменных
        if serial_number_last_digit.get() % 2 == 0:
            self.even = True
        else:
            self.even = False

        self.txt = ""

        # интерфейс
        self.row1 = Frame(self.top)
        Button(self.row1, bg="#f55353", width=10, height=2, command=self.write_red, font='20').pack(side=LEFT, pady=5, padx=5)
        Button(self.row1, bg="#5653f5", width=10, height=2, command=self.write_blue, font='20').pack(side=LEFT, pady=5, padx=5)
        Button(self.row1, bg="#f2f553", width=10, height=2, command=self.write_yellow, font='20').pack(side=LEFT, pady=5, padx=5)
        self.row1.pack()

        self.row2 = Frame(self.top)
        Button(self.row2, bg="#000", width=10, height=2, command=self.write_black, font='10').pack(side=LEFT, pady=5, padx=15)
        Button(self.row2, bg="#fff", width=10, height=2, command=self.write_white, font='10').pack(side=LEFT, pady=5, padx=15)
        self.row2.pack()

        self.row3 = Frame(self.top)
        Button(self.row3, text="Клик!", width=10, height=2, command=self.enter, font='10').pack(side=LEFT, pady=5, padx=15)
        Button(self.row3, text="clear", width=10, height=2, command=self.clear, font='10').pack(side=LEFT, pady=5, padx=15)
        self.row3.pack()

        self.lbl = Label(self.top, text="", font='50')
        self.lbl.pack(side=BOTTOM, pady=5)

    # когда нажимается кнопка, методы для запоминания порядка проводов и подсчёта их количества
    def write_red(self):
        self.txt += 'r'
        self.num_colors['r'] += 1

    def write_blue(self):
        self.txt += 'b'
        self.num_colors['b'] += 1

    def write_yellow(self):
        self.txt += 'y'
        self.num_colors['y'] += 1

    def write_black(self):
        self.txt += 'k'
        self.num_colors['k'] += 1

    def write_white(self):
        self.txt += 'w'
        self.num_colors['w'] += 1

    # делаем вывод, какой провод резать
    def enter(self):
        def split(word):
            return [char for char in word]

        txts = split(self.txt)
        number = len(txts)
        wires = []
        result = ""

        for wire in range(number):
            wires.append(txts[wire].lower())

        if number == 3:
            if 'r' not in wires:
                result += "Режь второй"
            elif wires[2] == 'w':
                result += "Режь последний"
            elif self.num_colors['b'] > 1:
                result += "Режь последний синий"
            else:
                result += "Режь последний"

        if number == 4:
            if self.num_colors['r'] > 1 and not self.even:
                result += "Режь последний красный"
            elif wires[3] == 'y' and self.num_colors['r'] == 0:
                result += "Режь первый"
            elif self.num_colors['b'] == 1:
                result += "Режь первый"
            elif self.num_colors['y'] > 1:
                result += "Режь последний"
            else:
                result += "Режь второй"

        if number == 5:
            if wires[4] == 'b' and self.even:
                result += "Режь четвёртый"
            elif self.num_colors['r'] == 1 and self.num_colors['y'] > 1:
                result += "Режь первый"
            elif self.num_colors['k'] == 0:
                result += "Режь второй"
            else:
                result += "Режь первый"

        if number == 6:
            if self.num_colors['y'] == 0 and not self.even:
                result += "Режь третий"
            elif self.num_colors['y'] == 1 and self.num_colors['w'] > 1:
                result += "Режь четвёртый"
            elif self.num_colors['r'] == 0:
                result += "Режь последний"
            else:
                result += "Режь четвёртый"

        self.lbl.configure(text=result)

    # если что-то пошло не так, то чистим все переменные, и вывод на всякий случай тоже "онуляем"
    def clear(self):
        self.txt = ""
        for i in self.num_colors:
            self.num_colors[i] = 0
        self.lbl.configure(text="")
