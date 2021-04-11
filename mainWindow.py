from password import *
from wires import *
from button import *


class Main:
    def __init__(self, master):
        self.master = master
        self.master.title('Солвер бомб')
        # self.master.geometry('400x300+200+150')

        self.num_of_batteries = IntVar()
        self.serial_number_last_digit = IntVar()
        self.is_parallel_port = BooleanVar()
        self.is_frk = BooleanVar()
        self.is_car = BooleanVar()

        self.row0 = tk.Frame()
        self.label_batteries = Label(self.row0, text='батарейки', width=10)
        self.label_batteries.pack(side=LEFT)
        self.label_serial = Label(self.row0, text='номер', width=10)
        self.label_serial.pack(side=LEFT)
        self.label_port = Label(self.row0, text='порт', width=10)
        self.label_port.pack(side=LEFT)
        self.label_FRK = Label(self.row0, text='FRK', width=10)
        self.label_FRK.pack(side=LEFT)
        self.label_car = Label(self.row0, text='car', width=10)
        self.label_car.pack(side=LEFT)
        self.row0.pack()

        self.row1 = tk.Frame()
        self.batteries_input = Entry(self.row1, textvariable=self.num_of_batteries, width=10)
        self.batteries_input.pack(side=LEFT)
        self.serial_input = Entry(self.row1, textvariable=self.serial_number_last_digit, width=10)
        self.serial_input.pack(side=LEFT)
        self.parallel_port = Checkbutton(self.row1, textvariable=self.is_parallel_port, width=10)
        self.parallel_port.pack(side=LEFT)
        self.frk_lamp = Checkbutton(self.row1, textvariable=self.is_frk, width=10)
        self.frk_lamp.pack(side=LEFT)
        self.car_lamp = Checkbutton(self.row1, textvariable=self.is_car, width=10)
        self.car_lamp.pack(side=LEFT)
        self.row1.pack()

        self.row2 = tk.Frame()
        self.button_wires = Button(self.row2, text='Провода', command=self.open_wires, width=15)
        self.button_wires.pack(side=LEFT)
        self.button_password = Button(self.row2, text='Пароль', command=self.open_password, width=15)
        self.button_password.pack(side=LEFT)
        self.button_button = Button(self.row2, text='Кнопка', command=self.open_button, width=15)
        self.button_button.pack(side=LEFT)
        self.button_key_board = Button(self.row2, text='Клавиатура', command=self.open_key_board, width=15)
        self.button_key_board.pack(side=LEFT)
        self.row2.pack()

        self.row3 = tk.Frame()
        self.button_colors = Button(self.row3, text='Делай как я', command=self.open_colors, width=15)
        self.button_colors.pack(side=LEFT)
        self.button_words = Button(self.row3, text='А вас как зовут', command=self.open_words, width=15)
        self.button_words.pack(side=LEFT)
        self.button_memory = Button(self.row3, text='Память', command=self.open_memory, width=15)
        self.button_memory.pack(side=LEFT)
        self.button_morse = Button(self.row3, text='Морзе', command=self.open_morse, width=15)
        self.button_morse.pack(side=LEFT)
        self.row3.pack()

        self.row4 = tk.Frame()
        self.button_wires_advanced = Button(self.row4, text='Усложненные провода', command=self.open_wires_advanced, width=31)
        self.button_wires_advanced.pack(side=LEFT)
        self.button_serial_wires = Button(self.row4, text='Последовательные провода', command=self.open_serial_wires, width=31)
        self.button_serial_wires.pack(side=LEFT)
        self.row4.pack()

        self.row5 = tk.Frame()
        self.button_maze = Button(self.row5, text='Лабиринт', command=self.open_maze, width=31)
        self.button_maze.pack(side=LEFT)
        self.button_rotary_handle = Button(self.row5, text='Поворотная ручка', command=self.open_rotary_handle, width=31)
        self.button_rotary_handle.pack(side=LEFT)
        self.row5.pack()

        self.master.mainloop()

    def open_wires(self):
        self.Wires = Wires(self.master, self.serial_number_last_digit)

    def open_password(self):
        self.Password = Password(self.master)

    def open_button(self):
        self.MyButton = MyButton(self.master, self.num_of_batteries, self.is_car, self.is_frk)

    def open_key_board(self):
        pass

    def open_colors(self):
        pass

    def open_words(self):
        pass

    def open_memory(self):
        pass

    def open_morse(self):
        pass

    def open_wires_advanced(self):
        pass

    def open_serial_wires(self):
        pass

    def open_maze(self):
        pass

    def open_rotary_handle(self):
        pass


if __name__ == '__main__':
    root = Tk()
    Main(root)
