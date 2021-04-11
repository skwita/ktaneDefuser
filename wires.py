from tkinter import *
from tkinter.ttk import Radiobutton


class Wires:
    def __init__(self, master):
        self.top = Toplevel(master)
        self.top.title('Провода')
        self.top.geometry('500x300+300+250')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)

        self.selected = IntVar()
        self.lbl = Label(self.top, text="")
        self.lbl.place(relx=.50, rely=.50, anchor='c')

        # self.rad3 = Radiobutton(self.top, text='Три', value=3, variable=self.selected)
        # self.rad4 = Radiobutton(self.top, text='Четыре', value=4, variable=self.selected)
        # self.rad5 = Radiobutton(self.top, text='Пять', value=5, variable=self.selected)
        # self.rad6 = Radiobutton(self.top, text='Шесть', value=6, variable=self.selected)
        #
        # self.rad3.place(relx=.25, rely=.0, anchor='n')
        # self.rad4.place(relx=.4, rely=.0, anchor='n')
        # self.rad5.place(relx=.55, rely=.0, anchor='n')
        # self.rad6.place(relx=.70, rely=.0, anchor='n')

        self.txt = string

        self.red = Button(self.top, bg="#f55353", width=10, height=2, command=self.write_red)
        self.red.place(relx=.5, rely=.1, anchor='c')
        self.blue = Button(self.top, bg="#5653f5", width=10, height=2)
        self.blue.place(relx=.5, rely=.25, anchor='c')
        self.yellow = Button(self.top, bg="#d4f553", width=10, height=2)
        self.yellow.place(relx=.5, rely=.4, anchor='c')
        self.white = Button(self.top, bg="#fff", width=10, height=2)
        self.white.place(relx=.5, rely=.55, anchor='c')

        self.btn = Button(self.top, text="Клик!", width=10, height=2, command=self.enter)
        self.btn.place(relx=.5, rely=.7, anchor='c')
        self.btn = Button(self.top, text="clear", width=10, height=2, command=self.clear)
        self.btn.place(relx=.5, rely=.845, anchor='c')

    def write_red(self):


    def enter(self):
        def split(word):
            return [char for char in word]

        number = self.selected.get()
        wires = []
        result = ""
        txts = split(self.txt.get())
        num_colors = {
            'r': 0,
            'b': 0,
            'e': 0,
            'k': 0,
            'w': 0
        }

        for wire in range(number):
            wires.append(txts[wire].lower())

        for wire in wires:
            if wire == 'r' or wire == 'к':
                num_colors['r'] += 1
            if wire == 'b' or wire == 'с':
                num_colors['b'] += 1
            if wire == 'e' or wire == 'ж':
                num_colors['e'] += 1
            if wire == 'k' or wire == 'ч':
                num_colors['k'] += 1
            if wire == 'w' or wire == 'б':
                num_colors['w'] += 1

        if number == 3:
            if ('r' or 'к') not in wires:
                result += "Режь второй"
            elif wires[2] == 'w' or wires[2] == 'б':
                result += "Режь последний"
            elif num_colors['b'] > 1:
                result += "Режь последний синий"
            else:
                result += "Режь последний"

        if number == 4:
            if num_colors['r'] > 1:
                result += "Если последняя цифра НЕчётная - режь последний красный"
                if (wires[3] == 'e' or wires[3] == 'ж') and num_colors['r'] == 0:
                    result += "Режь первый"
                elif num_colors['b'] == 1:
                    if result != "":
                        result += ", иначе режь первый"
                    else:
                        result += "Режь первый"
                elif num_colors['e'] > 1:
                    if result != "":
                        result += ", иначе режь последний"
                    else:
                        result += "Режь последний"
                elif result != "":
                    result += ", иначе режь второй"
                else:
                    result += "Режь второй"

        if number == 5:
            if wires[4] == 'b' or wires[4] == 'ч':
                result += "Если последняя цифра чётная - режь четвёртый"
                if num_colors['r'] == 1 and num_colors['e'] > 1:
                    if result != "":
                        result += ", иначе режь первый"
                    else:
                        result += "Режь первый"
                elif num_colors['k'] == 0:
                    if result != "":
                        result += ", иначе режь второй"
                    else:
                        result += "Режь второй"
                elif result != "":
                    result += ", иначе режь первый"
                else:
                    result += "Режь первый"

        if number == 6:
            if num_colors['e'] == 0:
                result += "Если последняя цифра НЕчётная - режь третий"
                if num_colors['e'] == 1 and num_colors['w'] > 1:
                    if result != "":
                        result += ", иначе режь четвёртыйй"
                    else:
                        result += "Режь четвёртый"
                elif num_colors['r'] == 0:
                    if result != "":
                        result += ", иначе режь последний"
                    else:
                        result += "Режь последний"
                elif result != "":
                    result += ", иначе режь четвёртый"
                else:
                    result += "Режь четвёртый"

        self.lbl.configure(text=result)

    def clear(self):
        self.txt.delete(0, END)
        self.lbl.configure(text="")


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    window = Wires(root)
    window.place()
    root.mainloop()
