from tkinter import *


class DoAsIDo:
    def __init__(self, master, is_vowels):
        self.top = Toplevel(master)
        self.top.title('Делай как я')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)

        # инструкции
        self.vow_zero = {
            'red': 'синий',
            'blue': 'красный',
            'green': 'жёлтый',
            'yellow': 'зелёный',
        }

        self.vow_one = {
            'red': 'жёлтый',
            'blue': 'зелёный',
            'green': 'синий',
            'yellow': 'красный',
        }

        self.vow_two = {
            'red': 'зелёный',
            'blue': 'красный',
            'green': 'жёлтый',
            'yellow': 'синий',
        }

        self.not_vow_zero = {
            'red': 'синий',
            'blue': 'жёлтый',
            'green': 'зелёный',
            'yellow': 'красный',
        }

        self.not_vow_one = {
            'red': 'красный',
            'blue': 'синий',
            'green': 'жёлтый',
            'yellow': 'зелёный',
        }

        self.not_vow_two = {
            'red': 'жёлтый',
            'blue': 'зелёный',
            'green': 'синий',
            'yellow': 'красный',
        }

        # инструкции в двумерном массиве для удобного программирования методов
        self.instructions = [[self.vow_zero, self.not_vow_zero],
                             [self.vow_one, self.not_vow_one],
                             [self.vow_two, self.not_vow_two]]

        # объявление переменных
        self.is_vowels = is_vowels.get()
        self.errors = IntVar()
        self.result = []
        self.history = []

        # интерфейс
        self.row0 = Frame(self.top)
        Label(self.row0, text="Ошибки: ").pack(side=LEFT)
        r0 = Radiobutton(self.row0, text='Нет', variable=self.errors, value=0, font='Arial 10')
        r0.pack(side=LEFT, padx=5)
        r1 = Radiobutton(self.row0, text='Одна', variable=self.errors, value=1, font='Arial 10')
        r1.pack(side=LEFT, padx=5)
        r2 = Radiobutton(self.row0, text='Две', variable=self.errors, value=2, font='Arial 10')
        r2.pack(side=LEFT, padx=5)
        self.row0.pack()

        self.row1 = Frame(self.top)
        Button(self.row1, text='Упс..', width=10, height=2, command=self.ooopsy, font='Arial 10').pack(side=LEFT, pady=5, padx=5)
        self.row1.pack()

        self.row2 = Frame(self.top)
        # красный
        Button(self.row2, bg="#f55353", width=10, height=2, command=self.red, font='Arial 10').pack(side=LEFT, pady=5, padx=5)
        # синий
        Button(self.row2, bg="#5653f5", width=10, height=2, command=self.blue, font='Arial 10').pack(side=LEFT, pady=5, padx=5)
        self.row2.pack()

        self.row3 = Frame(self.top)
        # зелёный
        Button(self.row3, bg="#53f563", width=10, height=2, command=self.green, font='Arial 10').pack(side=LEFT, pady=5, padx=5)
        # жёлтый
        Button(self.row3, bg="#f2f553", width=10, height=2, command=self.yellow, font='Arial 10').pack(side=LEFT, pady=5, padx=5)
        self.row3.pack()

        self.row4 = Frame(self.top)
        self.lbl = Label(self.row4, text='', font='Arial 10')
        self.lbl.pack()
        self.row4.pack()

    # нажали на красную кнопку
    def red(self):
        if self.is_vowels:
            instruction = self.instructions[self.errors.get()][0]
            result = instruction['red']
        else:
            instruction = self.instructions[self.errors.get()][1]
            result = instruction['red']
        self.history.append('red')
        self.result.append(result)
        result = self.merge(self.result)
        self.lbl.configure(text=result)

    # нажали на синюю кнопку
    def blue(self):
        if self.is_vowels:
            instruction = self.instructions[self.errors.get()][0]
            result = instruction['blue']
        else:
            instruction = self.instructions[self.errors.get()][1]
            result = instruction['blue']
        self.history.append('blue')
        self.result.append(result)
        result = self.merge(self.result)
        self.lbl.configure(text=result)

    # нажали на зелёную кнопку
    def green(self):
        if self.is_vowels:
            instruction = self.instructions[self.errors.get()][0]
            result = instruction['green']
        else:
            instruction = self.instructions[self.errors.get()][1]
            result = instruction['green']
        self.history.append('green')
        self.result.append(result)
        result = self.merge(self.result)
        self.lbl.configure(text=result)

    # нажали на жёлтую кнопку
    def yellow(self):
        if self.is_vowels:
            instruction = self.instructions[self.errors.get()][0]
            result = instruction['yellow']
        else:
            instruction = self.instructions[self.errors.get()][1]
            result = instruction['yellow']
        self.history.append('yellow')
        self.result.append(result)
        result = self.merge(self.result)
        self.lbl.configure(text=result)

    # формирования достойного ответа для игрока
    def merge(self, strings):
        res = ''
        for string in strings:
            res += string + ' '
        return res

    # если что-то пошло не так, то переписываем ответы для прожатых кнопок
    def ooopsy(self):
        colors = ['red', 'blue', 'green', 'yellow']
        new_result = []
        for what_was_pressed in self.history:
            for color in colors:
                if what_was_pressed == color:
                    if self.is_vowels:
                        instruction = self.instructions[self.errors.get()][0]
                        result = instruction[color]
                    else:
                        instruction = self.instructions[self.errors.get()][1]
                        result = instruction[color]
                    new_result.append(result)
        self.result = new_result
        result = self.merge(new_result)
        self.lbl.configure(text=result)
