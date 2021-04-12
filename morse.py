from tkinter import *


class Morse:
    def __init__(self, master):
        self.top = Toplevel(master)
        self.top.title('Морзе')
        self.frame = Frame(self.top)

        self.main_string = ""

        self.input = Label(self.top, width=45, height=1, bg='white')
        self.input.pack(padx=5, pady=5)

        self.row0 = Frame(self.top)
        self.point_button = Button(self.row0, text=".", command=self.inp_point, width=10).pack(side=LEFT, padx=5, pady=5)
        self.dash_button = Button(self.row0, text="-", command=self.inp_dash, width=10).pack(side=LEFT, padx=5, pady=5)
        self.space_button = Button(self.row0, text="⌴", command=self.inp_space, width=10).pack(side=LEFT, padx=5, pady=5)
        self.mistake_button = Button(self.row0, text="X", command=self.inp_mistake, width=10).pack(side=LEFT, padx=5, pady=5)
        self.row0.pack()

        self.row1 = Frame(self.top)
        self.parse_button = Button(self.row1, text="Parse", command=self.parse, width=22).pack(side=LEFT, padx=5, pady=5)
        self.clear_button = Button(self.row1, text="Clear", command=self.clear, width=22).pack(side=LEFT, padx=5, pady=5)
        self.row1.pack()

        self.output = Label(self.top, width=45, height=1, bg='#a5ff8f')
        self.output.pack(padx=5, pady=5)

    def inp_point(self):
        self.main_string += "."
        self.update_lbl()

    def inp_dash(self):
        self.main_string += "-"
        self.update_lbl()

    def inp_space(self):
        self.main_string += "   "
        self.update_lbl()

    def inp_mistake(self):
        self.main_string += "X"
        self.update_lbl()

    def update_lbl(self):
        self.input.configure(text=self.main_string)

    def parse(self):
        pass

    def clear(self):
        self.main_string = ""
        self.update_lbl()
