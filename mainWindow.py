from tkinter import *
from wires import *
from password import *


class Main:
    def __init__(self, master):
        self.master = master
        self.master.title('Солвер бомб')
        self.master.geometry('400x300+200+150')
        self.button_wires = Button(self.master, text='Провода', command=self.open_wires)
        self.button_wires.pack(side=BOTTOM)
        self.button_password = Button(self.master, text='Пароль', command=self.open_password)
        self.button_password.pack(side=BOTTOM)
        self.master.mainloop()

    def open_wires(self):
        self.Wires = Wires(self.master)

    def open_password(self):
        self.password = Password()


if __name__ == '__main__':
    root = Tk()
    Main(root)
