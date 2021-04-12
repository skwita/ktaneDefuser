from tkinter import *

class Memory:
    def __init__(self, master):
        self.top = Toplevel(master)
        self.top.title('Память')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)

        self.stage = 1
        self.value = False
        self.values = []
        self.positions = []
        self.num = StringVar()

        self.row1 = Frame(self.top)
        Button(self.row1, text='1', width=10, height=2, command=self.set_one).pack(side=LEFT, pady=5, padx=5)
        Button(self.row1, text='2', width=10, height=2, command=self.set_two).pack(side=LEFT, pady=5, padx=5)
        Button(self.row1, text='3', width=10, height=2, command=self.set_three).pack(side=LEFT, pady=5, padx=5)
        Button(self.row1, text='4', width=10, height=2, command=self.set_four).pack(side=LEFT, pady=5, padx=5)
        self.row1.pack()

        self.row2 = Frame(self.top)
        self.lbl1 = Label(self.row2, text='')
        self.lbl1.pack(side=LEFT, pady=5, padx=5)
        self.row2.pack()

        self.row3 = Frame(self.top)
        self.lbl2 = Label(self.row3, text='')
        self.lbl2.pack(side=LEFT, pady=5, padx=5)
        self.row3.pack()

        self.row4 = Frame(self.top)
        self.txt = Entry(self.row4, textvariable=self.num)
        self.txt.pack(side=LEFT, pady=5, padx=5)
        self.row4.pack()

        self.row4 = Frame(self.top)
        Button(self.row4, text='Клик!', width=10, height=2, command=self.enter).pack(side=LEFT, pady=5, padx=5)
        Button(self.row4, text='clear', width=10, height=2, command=self.clear).pack(side=LEFT, pady=5, padx=5)
        self.row4.pack()

    def set_one(self):
        if self.stage == 1:
            self.lbl1.configure(text="Нажмите на 2 позицию")
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(2)
        if self.stage == 2:
            self.lbl1.configure(text="Нажмите на 4")
            self.lbl2.configure(text="Позиция")
            self.value = False
            self.values.append(4)
        if self.stage == 3:
            self.lbl1.configure(text=("Нажмите на " + str(self.values[1])))
            self.lbl2.configure(text="Позиция")
            self.value = False
            self.values.append(self.values[1])
        if self.stage == 4:
            self.lbl1.configure(text=("Нажмите на " + str(self.positions[0]) + " позицию"))
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(self.positions[0])
        if self.stage == 5:
            self.lbl1.configure(text=("Нажмите на " + str(self.values[0])))
            self.lbl2.configure(text="Позиция")
        if self.stage > 5:
            self.lbl1.configure(text="ДУРАК")
            self.lbl2.configure(text="ЭТАПОВ ВСЕГО ПЯТЬ!!!!!")

        self.stage += 1

    def set_two(self):
        if self.stage == 1:
            self.lbl1.configure(text="Нажмите на 2 позицию")
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(2)
        if self.stage == 2:
            self.lbl1.configure(text=("Нажмите на " + str(self.positions[0]) + " позицию"))
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(self.positions[0])
        if self.stage == 3:
            self.lbl1.configure(text=("Нажмите на " + str(self.values[0])))
            self.lbl2.configure(text="Позиция")
            self.value = False
            self.values.append(self.values[0])
        if self.stage == 4:
            self.lbl1.configure(text="Нажмите на 1 позицию")
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(1)
        if self.stage == 5:
            self.lbl1.configure(text=("Нажмите на " + str(self.values[1])))
            self.lbl2.configure(text="Позиция")
        if self.stage > 5:
            self.lbl1.configure(text="ДУРАК")
            self.lbl2.configure(text="ЭТАПОВ ВСЕГО ПЯТЬ!!!!!")

        self.stage += 1

    def set_three(self):
        if self.stage == 1:
            self.lbl1.configure(text="Нажмите на 3 позицию")
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(3)
        if self.stage == 2:
            self.lbl1.configure(text="Нажмите на 1 позицию")
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(1)
        if self.stage == 3:
            self.lbl1.configure(text="Нажмите на 3 позицию")
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(3)
        if self.stage == 4:
            self.lbl1.configure(text=("Нажмите на " + str(self.positions[1]) + " позицию"))
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(self.positions[1])
        if self.stage == 5:
            self.lbl1.configure(text=("Нажмите на " + str(self.values[3])))
            self.lbl2.configure(text="Позиция")
        if self.stage > 5:
            self.lbl1.configure(text="ДУРАК")
            self.lbl2.configure(text="ЭТАПОВ ВСЕГО ПЯТЬ!!!!!")

    def set_four(self):
        if self.stage == 1:
            self.lbl1.configure(text="Нажмите на 4 позицию")
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(4)
        if self.stage == 2:
            self.lbl1.configure(text="Нажмите на " + str(self.positions[0]) + " позицию")
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(self.positions[0])
        if self.stage == 3:
            self.lbl1.configure(text="Нажмите на 4")
            self.lbl2.configure(text="Позиция")
            self.value = False
            self.values.append(4)
        if self.stage == 4:
            self.lbl1.configure(text=("Нажмите на " + str(self.positions[1]) + " позицию"))
            self.lbl2.configure(text="Значение")
            self.value = True
            self.positions.append(self.positions[1])
        if self.stage == 5:
            self.lbl1.configure(text=("Нажмите на " + str(self.values[2])))
            self.lbl2.configure(text="Позиция")
        if self.stage > 5:
            self.lbl1.configure(text="ДУРАК")
            self.lbl2.configure(text="ЭТАПОВ ВСЕГО ПЯТЬ!!!!!")


        self.stage += 1

    def enter(self):
        if self.value:
            self.values.append(int(self.num.get()))
        else:
            self.positions.append(int(self.num.get()))
        self.lbl1.configure(text="")
        self.lbl2.configure(text="")
        self.txt.delete(0, END)

    def clear(self):
        self.values.clear()
        self.positions.clear()
        self.stage = 1
        self.lbl1.configure(text="")
        self.lbl2.configure(text="")
        self.txt.delete(0, END)
