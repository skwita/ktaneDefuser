import tkinter as tk
from tkinter import ttk


class Words:
    main_word_array = ["YES", "FIRST", "ПУСТОЙ БЛИН", "DISPLAY",
                       "OKAY", "SAYS", "NOTHING", "BLANK", "NO",
                       "LED", "LEAD", "READ", "RED", "REED", "LEED",
                       "HOLD ON", "YOU", "YOU ARE", "YOUR", "YOU'RE",
                       "UR", "THERE", "THEY'RE", "THEIR", "THEY ARE",
                       "SEE", "C", "CEE"]

    word_array = ["READY", "FIRST", "NO", "BLANK", "NOTHING",
                  "YES", "WHAT", "UHHH", "LEFT", "RIGHT",
                  "MIDDLE", "OKAY", "WAIT", "PRESS", "YOU",
                  "YOU ARE", "YOUR", "YOU'RE", "UR", "U",
                  "UH HUH", "UH UH", "WHAT?", "DONE", "NEXT",
                  "HOLD", "SURE", "LIKE"]

    READY =         ["YES", "OKAY", "WHAT", "MIDDLE", "LEFT", "PRESS", "RIGHT", "BLANK", "READY", "NO", "FIRST", "UHHH", "NOTHING", "WAIT"]
    FIRST =         ["LEFT", "OKAY", "YES", "MIDDLE", "NO", "RIGHT", "NOTHING", "UHHH", "WAIT", "READY", "BLANK", "WHAT", "PRESS", "FIRST"]
    NO =            ["BLANK", "UHHH", "WAIT", "FIRST", "WHAT", "READY", "RIGHT", "YES", "NOTHING", "LEFT", "PRESS", "OKAY", "NO", "MIDDLE"]
    BLANK =         ["WAIT", "RIGHT", "OKAY", "MIDDLE", "BLANK", "PRESS", "READY", "NOTHING", "NO", "WHAT", "LEFT", "UHHH", "YES", "FIRST"]
    NOTHING =       ["UHHH", "RIGHT", "OKAY", "MIDDLE", "YES", "BLANK", "NO", "PRESS", "LEFT", "WHAT", "WAIT", "FIRST", "NOTHING", "READY"]
    YES =           ["OKAY", "RIGHT", "UHHH", "MIDDLE", "FIRST", "WHAT", "PRESS", "READY", "NOTHING", "YES", "LEFT", "BLANK", "NO", "WAIT"]
    WHAT =          ["UHHH", "WHAT", "LEFT", "NOTHING", "READY", "BLANK", "MIDDLE", "NO", "OKAY", "FIRST", "WAIT", "YES", "PRESS", "RIGHT"]
    UHHH =          ["READY", "NOTHING", "LEFT", "WHAT", "OKAY", "YES", "RIGHT", "NO", "PRESS", "BLANK", "UHHH", "MIDDLE", "WAIT", "FIRST"]
    LEFT =          ["RIGHT", "LEFT", "FIRST", "NO", "MIDDLE", "YES", "BLANK", "WHAT", "UHHH", "WAIT", "PRESS", "READY", "OKAY", "NOTHING"]
    RIGHT =         ["YES", "NOTHING", "READY", "PRESS", "NO", "WAIT", "WHAT", "RIGHT", "MIDDLE", "LEFT", "UHHH", "BLANK", "OKAY", "FIRST"]
    MIDDLE =        ["BLANK", "READY", "OKAY", "WHAT", "NOTHING", "PRESS", "NO", "WAIT", "LEFT", "MIDDLE", "RIGHT", "FIRST", "UHHH", "YES"]
    OKAY =          ["MIDDLE", "NO", "FIRST", "YES", "UHHH", "NOTHING", "WAIT", "OKAY", "LEFT", "READY", "BLANK", "PRESS", "WHAT", "RIGHT"]
    WAIT =          ["UHHH", "NO", "BLANK", "OKAY", "YES", "LEFT", "FIRST", "PRESS", "WHAT", "WAIT", "NOTHING", "READY", "RIGHT", "MIDDLE"]
    PRESS =         ["RIGHT", "MIDDLE", "YES", "READY", "PRESS", "OKAY", "NOTHING", "UHHH", "BLANK", "LEFT", "FIRST", "WHAT", "NO", "WAIT"]
    YOU =           ["SURE", "YOU ARE", "YOUR", "YOU'RE", "NEXT", "UH HUH", "UR", "HOLD", "WHAT?", "YOU", "UH UH", "LIKE", "DONE", "U"]
    YOU_ARE =       ["YOUR", "NEXT", "LIKE", "UH HUH", "WHAT?", "DONE", "UH UH", "HOLD", "YOU", "U", "YOU'RE", "SURE", "UR", "YOU ARE"]
    YOUR =          ["UH UH", "YOU ARE", "UH HUH", "YOUR", "NEXT", "UR", "SURE", "U", "YOU'RE", "YOU", "WHAT?", "HOLD", "LIKE", "DONE"]
    YOU_RE =        ["YOU", "YOU'RE", "UR", "NEXT", "UH UH", "YOU ARE", "U", "YOUR", "WHAT?", "UH HUH", "SURE", "DONE", "LIKE", "HOLD"]
    UR =            ["DONE", "U", "UR", "UH HUH", "WHAT?", "SURE", "YOUR", "HOLD", "YOU'RE", "LIKE", "NEXT", "UH UH", "YOU ARE", "YOU"]
    U =             ["UH HUH", "SURE", "NEXT", "WHAT?", "YOU'RE", "UR", "UH UH", "DONE", "U", "YOU", "LIKE", "HOLD", "YOU ARE", "YOUR"]
    UH_HUH =        ["UH HUH", "YOUR", "YOU ARE", "YOU", "DONE", "HOLD", "UH UH", "NEXT", "SURE", "LIKE", "YOU'RE", "UR", "U", "WHAT?"]
    UH_UH =         ["UR", "U", "YOU ARE", "YOU'RE", "NEXT", "UH UH", "DONE", "YOU", "UH HUH", "LIKE", "YOUR", "SURE", "HOLD", "WHAT?"]
    WHAT_question = ["YOU", "HOLD", "YOU'RE", "YOUR", "U", "DONE", "UH UH", "LIKE", "YOU ARE", "UH HUH", "UR", "NEXT", "WHAT?", "SURE"]
    DONE =          ["SURE", "UH HUH", "NEXT", "WHAT?", "YOUR", "UR", "YOU'RE", "HOLD", "LIKE", "YOU", "U", "YOU ARE", "UH UH", "DONE"]
    NEXT =          ["WHAT?", "UH HUH", "UH UH", "YOUR", "HOLD", "SURE", "NEXT", "LIKE", "DONE", "YOU ARE", "UR", "YOU'RE", "U", "YOU"]
    HOLD =          ["YOU ARE", "U", "DONE", "UH UH", "YOU", "UR", "SURE", "WHAT?", "YOU'RE", "NEXT", "HOLD", "UH HUH", "YOUR", "LIKE"]
    SURE =          ["YOU ARE", "DONE", "LIKE", "YOU'RE", "YOU", "HOLD", "UH HUH", "UR", "SURE", "U", "WHAT?", "NEXT", "YOUR", "UH UH"]
    LIKE =          ["YOU'RE", "NEXT", "U", "UR", "HOLD", "DONE", "UH UH", "WHAT?", "UH HUH", "YOU", "LIKE", "SURE", "YOU ARE", "YOUR"]

    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.title('Авас как зовут')
        self.frame = tk.Frame(self.top)
        self.word_array.sort()
        self.main_word_array.sort()

        self.main_combobox = ttk.Combobox(self.top, values=self.main_word_array)
        self.main_combobox.pack(padx=5, pady=5)

        self.row1 = tk.Frame(self.top)
        self.word_combobox1 = ttk.Combobox(self.row1, values=self.word_array, font='Arial 10')
        self.word_combobox1.pack(side='left', padx=5, pady=5)
        self.word_combobox2 = ttk.Combobox(self.row1, values=self.word_array, font='Arial 10')
        self.word_combobox2.pack(side='left', padx=5, pady=5)
        self.row1.pack()

        self.row2 = tk.Frame(self.top)
        self.word_combobox3 = ttk.Combobox(self.row2, values=self.word_array, font='Arial 10')
        self.word_combobox3.pack(side='left', padx=5, pady=5)
        self.word_combobox4 = ttk.Combobox(self.row2, values=self.word_array, font='Arial 10')
        self.word_combobox4.pack(side='left', padx=5, pady=5)
        self.row2.pack()

        self.row3 = tk.Frame(self.top)
        self.word_combobox5 = ttk.Combobox(self.row3, values=self.word_array, font='Arial 10')
        self.word_combobox5.pack(side='left', padx=5, pady=5)
        self.word_combobox6 = ttk.Combobox(self.row3, values=self.word_array, font='Arial 10')
        self.word_combobox6.pack(side='left', padx=5, pady=5)
        self.row3.pack()

        self.row4 = tk.Frame(self.top)
        self.btn_do = tk.Button(self.row4, text='определить!', command=self.proceed, font='Arial 10')
        self.btn_do.pack()
        self.row4.pack()

        self.row5 = tk.Frame(self.top)
        self.lbl = tk.Label(self.row5, font='Arial 10')
        self.lbl.pack(side='bottom')
        self.row5.pack()

    def proceed(self):
        main_word = self.main_combobox.get()
        word1 = self.word_combobox1.get()
        word2 = self.word_combobox2.get()
        word3 = self.word_combobox3.get()
        word4 = self.word_combobox4.get()
        word5 = self.word_combobox5.get()
        word6 = self.word_combobox6.get()
        current_word = ""
        work_array = []
        result = ""

        left_top = ["UR"]
        left_middle = ["YES", "NOTHING", "LED", "THEY ARE"]
        left_bottom = ["ПУСТОЙ БЛИН", "REED", "LEED", "THEY'RE"]
        right_top = ["FIRST", "OKAY", "C"]
        right_middle = ["READ", "BLANK", "RED", "YOU", "THEIR", "YOU'RE", "YOUR"]
        right_bottom = ["DISPLAY", "SAYS", "LEAD", "NO", "HOLD ON", "YOU ARE", "THERE", "SEE", "CEE"]

        if left_top.__contains__(main_word):
            current_word = word1
        elif right_top.__contains__(main_word):
            current_word = word2
        elif left_middle.__contains__(main_word):
            current_word = word3
        elif right_middle.__contains__(main_word):
            current_word = word4
        elif left_bottom.__contains__(main_word):
            current_word = word5
        elif right_bottom.__contains__(main_word):
            current_word = word6

        if current_word == "READY":
            work_array = self.READY.copy()
        elif current_word == "FIRST":
            work_array = self.FIRST.copy()
        elif current_word == "NO":
            work_array = self.NO.copy()
        elif current_word == "BLANK":
            work_array = self.BLANK.copy()
        elif current_word == "NOTHING":
            work_array = self.NOTHING.copy()
        elif current_word == "YES":
            work_array = self.YES.copy()
        elif current_word == "WHAT":
            work_array = self.WHAT.copy()
        elif current_word == "UHHH":
            work_array = self.UHHH.copy()
        elif current_word == "LEFT":
            work_array = self.LEFT.copy()
        elif current_word == "RIGHT":
            work_array = self.RIGHT.copy()
        elif current_word == "MIDDLE":
            work_array = self.MIDDLE.copy()
        elif current_word == "OKAY":
            work_array = self.OKAY.copy()
        elif current_word == "WAIT":
            work_array = self.WAIT.copy()
        elif current_word == "PRESS":
            work_array = self.PRESS.copy()
        elif current_word == "YOU":
            work_array = self.YOU.copy()
        elif current_word == "YOU ARE":
            work_array = self.YOU_ARE.copy()
        elif current_word == "YOUR":
            work_array = self.YOUR.copy()
        elif current_word == "YOU'RE":
            work_array = self.YOU_RE.copy()
        elif current_word == "UR":
            work_array = self.UR.copy()
        elif current_word == "U":
            work_array = self.U.copy()
        elif current_word == "UH HUH":
            work_array = self.UH_HUH.copy()
        elif current_word == "UH UH":
            work_array = self.UH_UH.copy()
        elif current_word == "WHAT?":
            work_array = self.WHAT_question.copy()
        elif current_word == "DONE":
            work_array = self.DONE.copy()
        elif current_word == "NEXT":
            work_array = self.NEXT.copy()
        elif current_word == "HOLD":
            work_array = self.HOLD.copy()
        elif current_word == "SURE":
            work_array = self.SURE.copy()
        elif current_word == "LIKE":
            work_array = self.LIKE.copy()

        for word in work_array:
            if word1 == word:
                result = word1
                break
            if word2 == word:
                result = word2
                break
            if word3 == word:
                result = word3
                break
            if word4 == word:
                result = word4
                break
            if word5 == word:
                result = word5
                break
            if word6 == word:
                result = word6
                break
        self.lbl.configure(text=result)
