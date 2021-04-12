from tkinter import *


class SerialWires:
    def __init__(self, master):
        self.top = Toplevel(master)
        self.top.title('Усложнённые провода')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)

        # массивы с решениями для каждого цвета
        self.decision_red = [['c'],
                             ['b'],
                             ['a'],
                             ['a', 'c'],
                             ['b'],
                             ['a', 'c'],
                             ['a', 'b', 'c'],
                             ['a', 'b'],
                             ['b']]

        self.decision_blue = [['b'],
                              ['a', 'c'],
                              ['b'],
                              ['a'],
                              ['b'],
                              ['b', 'c'],
                              ['c'],
                              ['a', 'c'],
                              ['a']]

        self.decision_black = [['a', 'b', 'c'],
                               ['a', 'c'],
                               ['b'],
                               ['a', 'c'],
                               ['b'],
                               ['b', 'c'],
                               ['a', 'b'],
                               ['c'],
                               ['c']]

        # количество попавшихся проводов
        self.count_red = -1
        self.count_blue = -1
        self.count_black = -1

        # нажатые цвет и буква
        self.current_let = ''
        self.current_color = ''

        # интерфейс
        self.row1 = Frame(self.top)
        Button(self.row1, bg="#f55353", command=self.inc_count_and_set_red, width=10, height=2, font='Arial 10').pack(side=LEFT, padx=5, pady=5)
        Button(self.row1, bg="#5653f5", command=self.inc_count_and_set_blue, width=10, height=2, font='Arial 10').pack(side=LEFT, padx=5, pady=5)
        Button(self.row1, bg="#000", command=self.inc_count_and_set_black, width=10, height=2, font='Arial 10').pack(side=LEFT, padx=5, pady=5)
        self.row1.pack()

        self.row2 = Frame(self.top)
        Button(self.row2, text="A", command=self.choose_a, width=10, height=2, font='Arial 10').pack(side=LEFT, padx=5, pady=5)
        Button(self.row2, text="B", command=self.choose_b, width=10, height=2, font='Arial 10').pack(side=LEFT, padx=5, pady=5)
        Button(self.row2, text="C", command=self.choose_c, width=10, height=2, font='Arial 10').pack(side=LEFT, padx=5, pady=5)
        self.row2.pack()

        self.row3 = Frame(self.top)
        Button(self.row3, text="Что делать?", command=self.must_do, width=10, height=2, font='Arial 10').pack(side=LEFT, padx=5, pady=5)
        Button(self.row3, text="Упс...", command=self.ooopsy, width=10, height=2, font='Arial 10').pack(side=LEFT, padx=5, pady=5)
        self.row3.pack()

        self.row4 = Frame(self.top)
        self.lbl = Label(self.row4, text='', font='Arial 10')
        self.lbl.pack(side=LEFT)
        self.row4.pack()

    def inc_count_and_set_red(self):
        self.count_red += 1
        self.current_color = 'red'

    def inc_count_and_set_blue(self):
        self.count_blue += 1
        self.current_color = 'blue'

    def inc_count_and_set_black(self):
        self.count_black += 1
        self.current_color = 'black'

    def choose_a(self):
        self.current_let = 'a'

    def choose_b(self):
        self.current_let = 'b'

    def choose_c(self):
        self.current_let = 'c'

    # вызывает кнопка "что делать"
    def must_do(self):
        result = ''
        colors = ['red', 'blue', 'black']
        decisions = [self.decision_red[self.count_red], self.decision_blue[self.count_blue], self.decision_black[self.count_black]]
        a = decisions[2]
        for i in range(3):
            if self.current_color == colors[i]:
                if self.current_let in decisions[i]:
                    result = 'Режь'
                else:
                    result = 'НЕ режь'

        self.lbl.configure(text=result)

    # вызывает кнопка упс
    def ooopsy(self):
        if self.current_color == 'red':
            self.count_red -= 1
        if self.current_color == 'blue':
            self.count_blue -= 1
        if self.current_color == 'black':
            self.count_black -= 1
        self.lbl.configure(text='')
