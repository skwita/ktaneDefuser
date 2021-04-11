from tkinter import *
from tkinter.ttk import Radiobutton


class Wires:
    def __init__(self, master, serial_number_last_digit):
        self.serial_number_last_digit = serial_number_last_digit.get()
        self.top = Toplevel(master)
        self.top.title('Провода')
        self.top.geometry('300x300+300+250')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)
        self.selected = IntVar()
        self.lbl = Label(self.top, text="")
        self.lbl.place(relx=0, rely=0, anchor='s')

        self.label = Label(self.top, text=self.serial_number_last_digit)
        self.label.pack(side=LEFT)

        self.rad3 = Radiobutton(self.top, text='Три', value=3, variable=self.selected)
        self.rad4 = Radiobutton(self.top, text='Четыре', value=4, variable=self.selected)
        self.rad5 = Radiobutton(self.top, text='Пять', value=5, variable=self.selected)
        self.rad6 = Radiobutton(self.top, text='Шесть', value=6, variable=self.selected)
        self.rad3.place(relx=.25, rely=.0, anchor='n')
        self.rad4.place(relx=.4, rely=.0, anchor='n')
        self.rad5.place(relx=.55, rely=.0, anchor='n')
        self.rad6.place(relx=.70, rely=.0, anchor='n')

        self.txt = Entry(self.top, width=30)
        self.txt.place(relx=.5, rely=.1, anchor='c')

        self.btn = Button(self.top, text="Клик!", command=self.enter)
        self.btn.place(relx=.5, rely=.2, anchor='c')
        self.btn = Button(self.top, text="clear", command=self.clear)
        self.btn.place(relx=.5, rely=.3, anchor='c')

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
