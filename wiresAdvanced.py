from tkinter import *
from PIL import ImageTk, Image


class WiresAdvanced:
    def __init__(self, master, serial_number_last_digit, parallel_port, num_battery):
        self.top = Toplevel(master)
        self.top.title('Кнопка')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)

        # объявление переменных
        if serial_number_last_digit.get() % 2 == 0:
            self.even = True
        else:
            self.even = False
        self.port = parallel_port.get()
        self.num_battery = num_battery.get()

        self.label_array = []
        self.label_array.append("РЕЖЬ РЕЖЬ РЕЖЬ РЕЖЬ РЕЖЬ")
        self.count = self.count_labels()

        # интерфейс
        for i in range(self.count):
            self.row = Frame(self.top)
            Label(self.row, text=self.label_array[i], font='Arial 20').pack(side=LEFT, pady=1, padx=15)
            self.row.pack()

        self.row = Frame(self.top)
        # забавная картинка
        self.img = ImageTk.PhotoImage(Image.open("resources\\meme.jpg"))
        Label(self.row, image=self.img).pack(side=LEFT, pady=1, padx=15)
        self.row.pack()

    # метод считает добавляет в массив строки и считает их количество
    def count_labels(self):
        self.label_array.append("Белый")
        self.label_array.append("Белый со звездой")
        self.label_array.append("Красный со звездой")
        count = 4

        if self.even:
            self.label_array.append("Красный")
            self.label_array.append("Синий")
            self.label_array.append("Красно-синий")
            self.label_array.append("Красно-синий горит")
            count += 4

        if self.port:
            self.label_array.append("Синий горит")
            self.label_array.append("Красно-синий со звездой")
            self.label_array.append("Синий со звездой горит")
            count += 3

        if self.num_battery > 2:
            self.label_array.append("Красный горит")
            self.label_array.append("Красный со звездой горит")
            self.label_array.append("Белый со звездой горит")
            count += 3
        return count
