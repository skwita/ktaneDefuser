import tkinter as tk
from functools import partial

from PIL import ImageTk, Image


class Keyboard:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.title('Клавиатура')
        self.frame = tk.Frame(self.top)
        self.row_array = list()

        self.links_array = ["resources\\a_s_pisechkoy.png", "resources\\abzac.png", "resources\\ae.png",
                            "resources\\ae_yo.png", "resources\\b.png", "resources\\c_s_tochkoy_vlevo.png",
                            "resources\\c_s_tochkoy_vpravo.png", "resources\\copyright.png", "resources\\i.png",
                            "resources\\i_kratkaya.png", "resources\\inoplanetyanin_stuchit.png", "resources\\j.png",
                            "resources\\lambda.png", "resources\\n_kursive.png", "resources\\neravno.png",
                            "resources\\o_kursive.png", "resources\\o_s_pisechkoy.png", "resources\\omega.png",
                            "resources\\question_mark_upside_down.png", "resources\\smailik.png",
                            "resources\\trezubets.png", "resources\\tverdiy_znak.png", "resources\\yaica.png",
                            "resources\\z.png", "resources\\zmeya.png", "resources\\zvezda_chernaya.png",
                            "resources\\zvezda_polaya.png"]
        self.buttons = list()
        self.images = list()
        self.presses = list()

        for i in range(5):
            row = tk.Frame(self.top)
            self.row_array.append(row)
            for j in range(7):
                if i * 7 + j < 27:
                    self.image = ImageTk.PhotoImage(Image.open(self.links_array[i * 7 + j]))
                    self.images.append(self.image)
                    self.array_button = tk.Button(self.row_array[i], image=self.images[i * 7 + j])
                    self.array_button.pack(side='left', fill='x', padx=5, pady=5)
                    self.buttons.append(self.array_button)
            self.row_array[i].pack(fill='x', expand=True)
        for i in range(27):
            self.buttons[i].configure(width=100, height=100, command=partial(self.save, i))

        self.row = tk.Frame(self.top)
        self.btn_final = tk.Button(self.row, text="click!", command=self.proceed).pack(side='left', padx=5, pady=5)
        self.btn_clear = tk.Button(self.row, text="clear", command=self.clear).pack(side='left', padx=5, pady=5)
        self.row.pack()

        self.row1 = tk.Frame(self.top)
        self.label_image1 = tk.Label(self.row1)
        self.label_image2 = tk.Label(self.row1)
        self.label_image3 = tk.Label(self.row1)
        self.label_image4 = tk.Label(self.row1)
        self.label_image1.pack(side='left')
        self.label_image2.pack(side='left')
        self.label_image3.pack(side='left')
        self.label_image4.pack(side='left')
        self.row1.pack()

    def save(self, i):
        self.presses.append(self.links_array[i])

    def proceed(self):
        columns = [["resources\\o_s_pisechkoy.png", "resources\\a_s_pisechkoy.png", "resources\\lambda.png",
                    "resources\\i.png", "resources\\inoplanetyanin_stuchit.png", "resources\\n_kursive.png",
                    "resources\\c_s_tochkoy_vlevo.png"],
                   ["resources\\ae_yo.png", "resources\\o_s_pisechkoy.png", "resources\\c_s_tochkoy_vlevo.png",
                    "resources\\o_kursive.png", "resources\\zvezda_polaya.png", "resources\\n_kursive",
                    "resources\\question_mark_upside_down.png"],
                   ["resources\\copyright.png", "resources\\yaica.png", "resources\\o_kursive.png",
                    "resources\\j.png", "resources\\z.png", "resources\\lambda.png",
                    "resources\\zvezda_polaya.png"],
                   ["resources\\b.png", "resources\\abzac.png", "resources\\tverdiy_znak.png",
                    "resources\\inoplanetyanin_stuchit.png", "resources\\j.png",
                    "resources\\question_mark_upside_down.png",
                    "resources\\smailik.png"],
                   ["resources\\trezubets.png", "resources\\smailik.png", "resources\\tverdiy_znak.png",
                    "resources\\c_s_tochkoy_vpravo.png", "resources\\abzac.png", "resources\\zmeya.png",
                    "resources\\zvezda_chernaya.png"],
                   ["resources\\b.png", "resources\\ae_yo.png", "resources\\neravno.png",
                    "resources\\ae.png", "resources\\trezubets.png", "resources\\i_kratkaya.png",
                    "resources\\omega.png"]]

        is_column = [True, True, True, True, True, True]
        for word in self.presses:
            if not columns[0].__contains__(word):
                is_column[0] = False
            if not columns[1].__contains__(word):
                is_column[1] = False
            if not columns[2].__contains__(word):
                is_column[2] = False
            if not columns[3].__contains__(word):
                is_column[3] = False
            if not columns[4].__contains__(word):
                is_column[4] = False
            if not columns[5].__contains__(word):
                is_column[5] = False
        temp = -1
        for i in range(len(is_column)):
            if is_column[i]:
                temp = i
        print(columns[temp])

        final = list()

        for word in columns[temp]:
            if self.presses.__contains__(word):
                final.append(word)

        print(final)
        if len(final) != 4:
            pass
        else:
            image1 = ImageTk.PhotoImage(Image.open(final[0]))
            self.label_image1.configure(image=image1)
            self.label_image1.photo_ref = image1
            image2 = ImageTk.PhotoImage(Image.open(final[1]))
            self.label_image2.configure(image=image2)
            self.label_image2.photo_ref = image2
            image3 = ImageTk.PhotoImage(Image.open(final[2]))
            self.label_image3.configure(image=image3)
            self.label_image3.photo_ref = image3
            image4 = ImageTk.PhotoImage(Image.open(final[3]))
            self.label_image4.configure(image=image4)
            self.label_image4.photo_ref = image4
        self.presses.clear()

    def clear(self):

        self.label_image1.configure(image=ImageTk.PhotoImage(Image.open("resources\\meme.jpg")))
        self.label_image2.configure(image=ImageTk.PhotoImage(Image.open("resources\\meme.jpg")))
        self.label_image3.configure(image=ImageTk.PhotoImage(Image.open("resources\\meme.jpg")))
        self.label_image4.configure(image=ImageTk.PhotoImage(Image.open("resources\\meme.jpg")))
