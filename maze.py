from tkinter import *
from tkinter.ttk import Combobox
import copy


class Maze:
    # класс игрока, хранит в себе местоположение и историю перемещения
    class Player:
        def __init__(self, row, column):
            self.row = row
            self.column = column
            self.history = []

        def mark_up(self, maze, row, column):
            maze[row][column] = 9

        def come(self, maze, row, column):
            maze[row][column] = 9
            self.row = row
            self.column = column
            self.history.append([row, column])

        def can_move_left(self, maze):
            if maze[self.row][self.column - 1] == 0:
                return True
            return False

        def can_move_right(self, maze):
            if maze[self.row][self.column + 1] == 0:
                return True
            return False

        def can_move_up(self, maze):
            if maze[self.row - 1][self.column] == 0:
                return True
            return False

        def can_move_down(self, maze):
            if maze[self.row + 1][self.column] == 0:
                return True
            return False

    # сборник анекдотов (лабиринтов)
    maze1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
             [1, 2, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    maze2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
             [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    maze3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    maze4 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 1, 2, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 0, 2, 1, 0, 0, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    maze5 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 1, 2, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    maze6 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    maze7 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 2, 1, 0, 1, 2, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    maze8 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
             [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1, 2, 1, 0, 1, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    maze9 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 2, 0, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
             [1, 2, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    # /сборник анекдотов

    # расположение ключевых кругов в лабиринтах
    mazes = {
        "3, 1": maze1,
        "5, 11": maze1,
        "1, 1": maze2,
        "7, 1": maze2,
        "1, 3": maze3,
        "11, 3": maze3,
        "3, 9": maze4,
        "7, 3": maze4,
        "5, 9": maze5,
        "11, 7": maze5,
        "1, 7": maze6,
        "7, 5": maze6,
        "7, 7": maze7,
        "7, 11": maze7,
        "1, 9": maze8,
        "9, 5": maze8,
        "3, 5": maze9,
        "9, 1": maze9,
    }

    # строка, столбик
    numbers = [6, 5, 4, 3, 2, 1]

    def __init__(self, master):
        self.top = Toplevel(master)
        self.top.title('Лабиринт')
        self.frame = Frame(self.top)
        self.frame.pack(side=BOTTOM)

        # создание интерфейса
        self.row1 = Frame(self.top)
        Label(self.row1, text='Ориентировочный круг:').pack()
        self.row1.pack()

        self.row2 = Frame(self.top)
        Label(self.row2, text='Строка:', font='Arial 10').pack(side='left', padx=5, pady=5)
        self.row_circle = Combobox(self.row2, values=self.numbers, font='Arial 10')
        self.row_circle.pack(side='left', padx=5, pady=5)
        self.row2.pack()

        self.row3 = Frame(self.top)
        Label(self.row3, text='Столбик:', font='Arial 10').pack(side='left', padx=5, pady=5)
        self.column_circle = Combobox(self.row3, values=self.numbers, font='Arial 10')
        self.column_circle.pack(side='left', padx=5, pady=5)
        self.row3.pack()

        self.row4 = Frame(self.top)
        Label(self.row4, text='Игрок:', font='Arial 10').pack()
        self.row4.pack()

        self.row5 = Frame(self.top)
        Label(self.row5, text='Строка:', font='Arial 10').pack(side='left', padx=5, pady=5)
        self.row_player = Combobox(self.row5, values=self.numbers, font='Arial 10')
        self.row_player.pack(side='left', padx=5, pady=5)
        self.row5.pack()

        self.row6 = Frame(self.top)
        Label(self.row6, text='Столбик:', font='Arial 10').pack(side='left', padx=5, pady=5)
        self.column_player = Combobox(self.row6, values=self.numbers, font='Arial 10')
        self.column_player.pack(side='left', padx=5, pady=5)
        self.row6.pack()

        self.row7 = Frame(self.top)
        Label(self.row7, text='Цель:', font='Arial 10').pack()
        self.row7.pack()

        self.row8 = Frame(self.top)
        Label(self.row8, text='Строка:', font='Arial 10').pack(side='left', padx=5, pady=5)
        self.row_ambition = Combobox(self.row8, values=self.numbers, font='Arial 10')
        self.row_ambition.pack(side='left', padx=5, pady=5)
        self.row8.pack()

        self.row9 = Frame(self.top)
        Label(self.row9, text='Столбик:', font='Arial 10').pack(side='left', padx=5, pady=5)
        self.column_ambition = Combobox(self.row9, values=self.numbers, font='Arial 10')
        self.column_ambition.pack(side='left', padx=5, pady=5)
        self.row9.pack()

        self.row10 = Frame(self.top)
        Button(self.row10, text='Найти путь!', command=self.solve_maze, width=15, font='Arial 10').pack(side=LEFT, padx=5, pady=5)
        self.row10.pack()

        self.row11 = Frame(self.top)
        self.solution = Label(self.row11, text='', font='Arial 10')
        self.solution.pack()
        self.row11.pack()

    def solve_maze(self):
        # получаем значения строчек и стобликов
        row_circle = int(self.row_circle.get()) * 2 - 1
        column_circle = int(self.column_circle.get()) * 2 - 1
        row_player = int(self.row_player.get()) * 2 - 1
        column_player = int(self.column_player.get()) * 2 - 1
        row_ambition = int(self.row_ambition.get()) * 2 - 1
        column_ambition = int(self.column_ambition.get()) * 2 - 1

        # определяем, какой лабиринт надо проходить
        to_search = str(row_circle) + ', ' + str(column_circle)
        maze = self.mazes[to_search]

        # создание самого первого игрока
        player = self.Player(row_player, column_player)
        # поиск пути
        result = self.find_way(maze.copy(), copy.deepcopy(player), player.row, player.column, row_ambition, column_ambition)
        # вывод результата
        if result is None:
            self.solution.configure(text='Выхода нет.')
        else:
            finally_result = self.transformation(result)
            self.solution.configure(text=finally_result + ' Я УВЕРЕН')

    def find_way(self, maze, player, row, column, row_ambition, column_ambition):
        # копируем лабиринт
        maze_clone = copy.deepcopy(maze)
        # помечаем текущую клетку как пройденную
        player.come(maze_clone, row, column)

        # если пришли, возвращаем историю
        if player.row == row_ambition and player.column == column_ambition:
            return player.history

        # рекурсивный алгоритм поиска пути
        if player.can_move_left(maze_clone):
            # помечаем промежуточную клетку, как пройденную
            player.mark_up(maze_clone, row, column - 1)
            check = self.find_way(maze_clone, copy.deepcopy(player), player.row, player.column - 2, row_ambition, column_ambition)
            if check is not None:
                return check
        if player.can_move_right(maze_clone):
            player.mark_up(maze_clone, row, column + 1)
            check = self.find_way(maze_clone, copy.deepcopy(player), player.row, player.column + 2, row_ambition, column_ambition)
            if check is not None:
                return check
        if player.can_move_up(maze_clone):
            player.mark_up(maze_clone, row - 1, column)
            check = self.find_way(maze_clone, copy.deepcopy(player), player.row - 2, player.column, row_ambition, column_ambition)
            if check is not None:
                return check
        if player.can_move_down(maze_clone):
            player.mark_up(maze_clone, row + 1, column)
            check = self.find_way(maze_clone, copy.deepcopy(player), player.row + 2, player.column, row_ambition, column_ambition)
            if check is not None:
                return check

    # функция для перевода массива передвижений в текст
    def transformation(self, array):
        manual = ''
        previous = ''
        count = 0
        for i in range(1, len(array)):
            if array[i][1] < array[i - 1][1]:
                # "влево":
                if previous == "влево":
                    count += 1
                elif count == 1:
                    manual += previous + ', '
                else:
                    manual += str(count) + ' ' + previous + ', '
                    count = 1
                previous = "влево"

            if array[i][1] > array[i - 1][1]:
                # "вправо":
                if previous == "вправо":
                    count += 1
                elif count == 1:
                    manual += previous + ', '
                else:
                    manual += str(count) + ' ' + previous + ', '
                    count = 1
                previous = "вправо"

            if array[i][0] < array[i - 1][0]:
                # "вверх":
                if previous == "вверх":
                    count += 1
                elif count == 1:
                    manual += previous + ', '
                else:
                    manual += str(count) + ' ' + previous + ', '
                    count = 1
                previous = "вверх"

            if array[i][0] > array[i - 1][0]:
                # "вниз":
                if previous == "вниз":
                    count += 1
                elif count == 1:
                    manual += previous + ', '
                else:
                    manual += str(count) + ' ' + previous + ', '
                    count = 1
                previous = "вниз"

        if count == 1:
            manual += previous
        else:
            manual += str(count) + ' ' + previous
        manual = manual[3:]

        return manual
