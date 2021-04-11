import tkinter as tk


class Password(tk.Frame):
    allWords = ["about", "after", "again", "below", "could",
                "every", "first", "found", "great", "house",
                "large", "learn", "never", "other", "place",
                "plant", "point", "right", "small", "sound",
                "spell", "still", "study", "their", "there",
                "these", "thing", "think", "three", "water",
                "where", "which", "world", "would", "write"]

    def __init__(self):
        super().__init__()
        row_array = list()
        for i in range(7):
            row = tk.Frame(self)
            row_array.append(row)

        self.labels = list()
        self.t1 = tk.StringVar()
        self.t2 = tk.StringVar()
        self.t3 = tk.StringVar()
        self.t4 = tk.StringVar()
        # root.geometry('500x500')
        for i in range(7):
            for j in range(5):
                self.array_label = tk.Label(row_array[i], width=7, text=self.allWords[i * 5 +j])
                self.array_label.pack(side='left', fill='x')
                self.labels.append(self.array_label)
            row_array[i].pack(fill='x', expand=True)

        self.txt1 = tk.Entry(self, textvariable=self.t1)
        self.txt1.pack(fill='x', expand=True)
        self.txt2 = tk.Entry(self, textvariable=self.t2)
        self.txt2.pack(fill='x', expand=True)
        self.txt3 = tk.Entry(self, textvariable=self.t3)
        self.txt3.pack(fill='x', expand=True)
        self.txt4 = tk.Entry(self, textvariable=self.t4)
        self.txt4.pack(fill='x', expand=True)
        self.btn = tk.Button(self, text="clear", command=self.clear)
        self.btn.pack(anchor='center')

        self.t1.trace("w", lambda name, index, mode, t1=self.t1: self.enter())
        self.t2.trace("w", lambda name, index, mode, t2=self.t2: self.enter())
        self.t3.trace("w", lambda name, index, mode, t3=self.t3: self.enter())
        self.t4.trace("w", lambda name, index, mode, t4=self.t4: self.enter())

    def enter(self):
        result1 = list()
        result2 = list()
        result3 = list()
        result4 = list()

        def split(the_word):
            return [char for char in the_word]

        if self.txt1.get() is not None:
            first = split(self.txt1.get())
        if self.txt2.get() is not None:
            second = split(self.txt2.get())
        if self.txt3.get() is not None:
            third = split(self.txt3.get())
        if self.txt4.get() is not None:
            fourth = split(self.txt4.get())

        for a in first:
            for word in self.allWords:
                if a == word[0]:
                    result1.append(word)
        for b in second:
            for word in self.allWords:
                if b == word[1]:
                    result2.append(word)
        for c in third:
            for word in self.allWords:
                if c == word[2]:
                    result3.append(word)
        for d in fourth:
            for word in self.allWords:
                if d == word[3]:
                    result4.append(word)

        final = list()
        word1 = False
        word2 = False
        word3 = False
        word4 = False

        if self.txt1.get() == "":
            word1 = False
        else:
            word1 = True
        if self.txt2.get() == "":
            word2 = False
        else:
            word2 = True
        if self.txt3.get() == "":
            word3 = False
        else:
            word3 = True
        if self.txt4.get() == "":
            word4 = False
        else:
            word4 = True

        final = self.allWords.copy()

        for i in range(len(self.allWords)):
            if word1:
                if not result1.__contains__(self.allWords[i]) and final.__contains__(self.allWords[i]):
                    final.pop(final.index(self.allWords[i]))
            if word2:
                if not result2.__contains__(self.allWords[i]) and final.__contains__(self.allWords[i]):
                    final.pop(final.index(self.allWords[i]))
            if word3:
                if not result3.__contains__(self.allWords[i]) and final.__contains__(self.allWords[i]):
                    final.pop(final.index(self.allWords[i]))
            if word4:
                if not result4.__contains__(self.allWords[i]) and final.__contains__(self.allWords[i]):
                    final.pop(final.index(self.allWords[i]))

        for i in range(len(self.allWords)):
            if final.__contains__(self.labels[i].cget("text")):
                self.labels[i].configure(bg="#a5ff8f")
            else:
                self.labels[i].configure(bg="#ffa6a6")

        result1.clear()
        result2.clear()
        result3.clear()
        result4.clear()

    def clear(self):
        self.txt1.delete(0, tk.END)
        self.txt2.delete(0, tk.END)
        self.txt3.delete(0, tk.END)
        self.txt4.delete(0, tk.END)
        for i in range(len(self.allWords)):
            self.labels[i].configure(bg="#ffa6a6")


if __name__ == '__main__':
    root = tk.Tk()
    app = Password()
    app.pack()
    root.mainloop()
