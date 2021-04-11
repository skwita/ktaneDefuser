from tkinter import *
from wires import *
from password import *


class Main:
    def __init__(self, master):
        self.master = master
        self.master.title('Солвер бомб')
        self.master.geometry('400x300+200+150')

        self.num_of_batteries = StringVar()
        self.serial_number_last_digit = StringVar()
        self.is_parallel_port = StringVar()

        self.batteries_input = Entry(self.master, textvariable=self.serial_number_last_digit)
        self.batteries_input.pack(side=TOP)

        self.temp = Label(self.master)
        self.temp.pack(side=TOP)

        self.button_wires = Button(self.master, text='Провода', command=self.open_wires)
        self.button_wires.pack(side=BOTTOM)
        self.button_password = Button(self.master, text='Пароль', command=self.open_password)
        self.button_password.pack(side=BOTTOM)

        self.master.mainloop()

    def open_wires(self):
        self.Wires = Wires(self.master, self.serial_number_last_digit)

    def open_password(self):
        self.password = Password(self.master)


if __name__ == '__main__':
    root = Tk()
    Main(root)
