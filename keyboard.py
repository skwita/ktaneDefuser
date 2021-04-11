import tkinter as tk

from PIL import ImageTk, Image


class Keyboard:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.title('Пароль')
        self.frame = tk.Frame(self.top)
        self.row_array = list()

        self.links_array = ["resources\\a_s_pisechkoy.jpg", "resources\\abzac.jpg", "resources\\ae.jpg",
                       "resources\\ae_yo.jpg", "resources\\b.jpg", "resources\\c_ s_tochkoy_vlevo.jpg",
                       "resources\\c_s_tochkoy_vpravo.jpg", "resources\\copyright.jpg", "resources\\i.jpg",
                       "resources\\i_kratkaya.jpg", "resources\\inoplanetyanin_stuchit.jpg", "resources\\j.jpg",
                       "resources\\lambda.jpg", "resources\\n_kursive.jpg", "resources\\neravno.jpg",
                       "resources\\o_kursive.jpg", "resources\\o_s_pisechkoy.jpg", "resources\\omega.jpg",
                       "resources\\question_mark_upside_down.jpg", "resources\\smailik.jpg", "resources\\trezubets.jpg",
                       "resources\\tverdiy_znak.jpg", "resources\\yaica.jpg", "resources\\z.jpg",
                       "resources\\zmeya.jpg", "resources\\zvezda_chernaya.jpg", "resources\\zvezda_polaya.jpg"]

        self.buttons = list()
        for i in range(4):
            row = tk.Frame(self.top)
            self.row_array.append(row)
            for j in range(7):
                self.image = open(self.links_array[i * 7 + j])
                self.array_button = tk.Button(image=self.image)
                self.array_button.pack(side='left', fill='x')
                self.buttons.append(self.array_button)
            self.row_array[i].pack(fill='x', expand=True)
