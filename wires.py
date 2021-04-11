from tkinter import *
from tkinter.ttk import Radiobutton


class Wires:
    def __init__(self, master, serial_number_last_digit):
        self.top = Toplevel(master)
        self.top.title('Провода')
        self.top.geometry('110x320+300+250')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)

        if int(serial_number_last_digit.get()) % 2 == 0:
            self.even = True
        else:
            self.even = False

        self.num_colors = {
            'r': 0,
            'b': 0,
            'y': 0,
            'k': 0,
            'w': 0
        }
        self.lbl = Label(self.top, text="")
        self.lbl.place(relx=.50, rely=.95, anchor='c')

        self.txt = ""

        self.red = Button(self.top, bg="#f55353", width=10, height=2, command=self.write_red)
        self.red.place(relx=.5, rely=.1, anchor='c')

        self.blue = Button(self.top, bg="#5653f5", width=10, height=2, command=self.write_blue)
        self.blue.place(relx=.5, rely=.25, anchor='c')

        self.yellow = Button(self.top, bg="#d4f553", width=10, height=2, command=self.write_yellow)
        self.yellow.place(relx=.5, rely=.4, anchor='c')

        self.black = Button(self.top, bg="#fff", width=10, height=2, command=self.write_black)
        self.black.place(relx=.5, rely=.55, anchor='c')

        self.white = Button(self.top, bg="#fff", width=10, height=2, command=self.write_white)
        self.white.place(relx=.5, rely=.55, anchor='c')

        self.btn = Button(self.top, text="Клик!", width=10, height=2, command=self.enter)
        self.btn.place(relx=.5, rely=.7, anchor='c')
        self.btn = Button(self.top, text="clear", width=10, height=2, command=self.clear)
        self.btn.place(relx=.5, rely=.845, anchor='c')

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

    def clear(self):
        self.txt = ""
        self.lbl.configure(text="")


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    window = Wires(root)
    window.place()
    root.mainloop()
