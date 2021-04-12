from morse import Morse
from password import *
from rotaryHandle import RotaryHandle
from wires import *
from words import Words
from button import *
from wiresAdvanced import *
from memory import *
from keyboard import *
from maze import *
from serialWires import *
from doAsIDo import *


class Main:
    def __init__(self, master):
        self.master = master
        self.master.title('Солвер бомб')

        self.num_of_batteries = IntVar()
        self.serial_number_last_digit = IntVar()
        self.is_parallel_port = BooleanVar()
        self.is_frk = BooleanVar()
        self.is_car = BooleanVar()
        self.is_vowels = BooleanVar()

        self.row0 = tk.Frame()
        Label(self.row0, text='порт', width=5).pack(side=LEFT)
        Checkbutton(self.row0, variable=self.is_parallel_port, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Label(self.row0, text='гласные').pack(side=LEFT, padx=11)
        Checkbutton(self.row0, variable=self.is_vowels, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        self.row0.pack(anchor=W)

        self.row1 = tk.Frame()
        Label(self.row1, text='car', width=5).pack(side=LEFT)
        Checkbutton(self.row1, variable=self.is_car, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Label(self.row1, text='батарейки', width=11).pack(side=LEFT)
        Entry(self.row1, textvariable=self.num_of_batteries, width=11).pack(side=LEFT)
        self.row1.pack(anchor=W)

        self.row2 = tk.Frame()
        Label(self.row2, text='FRK', width=5).pack(side=LEFT)
        Checkbutton(self.row2, variable=self.is_frk, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Label(self.row2, text='номер', width=11).pack(side=LEFT)
        Entry(self.row2, textvariable=self.serial_number_last_digit, width=11).pack(side=LEFT)
        self.row2.pack(anchor=W)

        self.row3 = tk.Frame()
        Button(self.row3, text='Провода', command=self.open_wires, width=15).pack(side=LEFT, padx=5, pady=5)
        Button(self.row3, text='Пароль', command=self.open_password, width=15).pack(side=LEFT, padx=5, pady=5)
        Button(self.row3, text='Кнопка', command=self.open_button, width=15).pack(side=LEFT, padx=5, pady=5)
        Button(self.row3, text='Клавиатура', command=self.open_key_board, width=15).pack(side=LEFT, padx=5, pady=5)
        self.row3.pack()

        self.row4 = tk.Frame()
        Button(self.row4, text='Делай как я', command=self.open_colors, width=15).pack(side=LEFT, padx=5, pady=5)
        Button(self.row4, text='А вас как зовут', command=self.open_words, width=15).pack(side=LEFT, padx=5, pady=5)
        Button(self.row4, text='Память', command=self.open_memory, width=15).pack(side=LEFT, padx=5, pady=5)
        Button(self.row4, text='Морзе', command=self.open_morse, width=15).pack(side=LEFT, padx=5, pady=5)
        self.row4.pack()

        self.row5 = tk.Frame()
        Button(self.row5, text='Усложненные провода', command=self.open_wires_advanced, width=33).pack(side=LEFT, padx=5, pady=5)
        Button(self.row5, text='Последовательные провода', command=self.open_serial_wires, width=33).pack(side=LEFT, padx=5, pady=5)
        self.row5.pack()

        self.row6 = tk.Frame()
        Button(self.row6, text='Лабиринт', command=self.open_maze, width=33).pack(side=LEFT, padx=5, pady=5)
        Button(self.row6, text='Поворотная ручка', command=self.open_rotary_handle, width=33).pack(side=LEFT, padx=5, pady=5)
        self.row6.pack()

        self.master.mainloop()

    def open_wires(self):
        self.Wires = Wires(self.master, self.serial_number_last_digit)

    def open_password(self):
        self.Password = Password(self.master)

    def open_button(self):
        self.MyButton = MyButton(self.master, self.num_of_batteries, self.is_car, self.is_frk)

    def open_key_board(self):
        self.Keyboard = Keyboard(self.master)

    def open_colors(self):
        self.DoAsIDo = DoAsIDo(self.master, self.is_vowels)

    def open_words(self):
        self.Words = Words(self.master)

    def open_memory(self):
        self.Memory = Memory(self.master)

    def open_morse(self):
        self.Morse = Morse(self.master)

    def open_wires_advanced(self):
        self.WiresAdvanced = WiresAdvanced(self.master, self.serial_number_last_digit, self.is_parallel_port, self.num_of_batteries)

    def open_serial_wires(self):
        self.SerialWires = SerialWires(self.master)

    def open_maze(self):
        self.Maze = Maze(self.master)

    def open_rotary_handle(self):
        self.RotaryHandle = RotaryHandle(self.master)


if __name__ == '__main__':
    root = Tk()
    Main(root)
