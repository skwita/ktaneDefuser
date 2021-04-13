from tkinter import *


class Morse:
    def __init__(self, master):
        self.top = Toplevel(master)
        self.top.title('Морзе')
        self.frame = Frame(self.top)

        self.decodes = {
            '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd',
            '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
            '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
            '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
            '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
            '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
            '-.--': 'y', '--..': 'z'
        }

        self.morse_codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-',
                            '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
                            '-.--', '--..']

        self.words_frequencies = {
            'shell': '3.505 MHz', 'halls': '3.515 MHz', 'slick': '3.522 MHz', 'trick': '3.532 MHz',
            'boxes': '3.535 MHz', 'leaks': '3.542 MHz', 'strobe': '3.545 MHz', 'bistro': '3.552 MHz',
            'flick': '3.555 MHz', 'bombs': '3.565 MHz', 'break': '3.572 MHz', 'brick': '3.575 MHz',
            'steak': '3.582 MHz', 'sting': '3.592 MHz', 'vector': '3.595 MHz', 'beats': '3.600 MHz'
        }

        self.words = ['shell', 'halls', 'slick', 'trick', 'boxes', 'leaks', 'strobe', 'bistro', 'flick',
                      'bombs', 'break', 'brick', 'steak', 'sting', 'vector', 'beats']

        self.frequencies = ['3.505 MHz', '3.515 MHz', '3.522 MHz', '3.532 MHz', '3.535 MHz', '3.542 MHz',
                            '3.545 MHz', '3.552 MHz', '3.555 MHz', '3.565 MHz', '3.572 MHz', '3.575 MHz',
                            '3.582 MHz', '3.592 MHz', '3.595 MHz', '3.600 MHz']

        self.letter1 = StringVar()
        self.letter2 = StringVar()
        self.letter3 = StringVar()
        self.letter4 = StringVar()
        self.letter5 = StringVar()

        row_array = list()

        for i in range(4):
            row = Frame(self.top)
            row_array.append(row)

        self.labels = list()

        for i in range(4):
            for j in range(4):
                self.array_label = Label(row_array[i], width=10, text=self.frequencies[i * 4 + j], font='20')
                self.array_label.pack(side=LEFT, pady=5, padx=5)
                self.labels.append(self.array_label)
            row_array[i].pack(side=TOP)

        self.row = Frame(self.top)
        self.input0 = Entry(self.row, width=20, bg='white', textvariable=self.letter1)
        self.input0.pack(padx=5, pady=5, side=LEFT)
        self.label0 = Label(self.row, width=3)
        self.label0.pack(side=LEFT, pady=5, padx=5)
        self.row.pack()

        self.row = Frame(self.top)
        self.input1 = Entry(self.row, width=20, bg='white', textvariable=self.letter2)
        self.input1.pack(padx=5, pady=5, side=LEFT)
        self.label1 = Label(self.row, width=3)
        self.label1.pack(side=LEFT, pady=5, padx=5)
        self.row.pack()

        self.row = Frame(self.top)
        self.input2 = Entry(self.row, width=20, bg='white', textvariable=self.letter3)
        self.input2.pack(padx=5, pady=5, side=LEFT)
        self.label2 = Label(self.row, width=3)
        self.label2.pack(side=LEFT, pady=5, padx=5)
        self.row.pack()

        self.row = Frame(self.top)
        self.input3 = Entry(self.row, width=20, bg='white', textvariable=self.letter4)
        self.input3.pack(padx=5, pady=5, side=LEFT)
        self.label3 = Label(self.row, width=3)
        self.label3.pack(side=LEFT, pady=5, padx=5)
        self.row.pack()

        self.row = Frame(self.top)
        self.input4 = Entry(self.row, width=20, bg='white', textvariable=self.letter5)
        self.input4.pack(padx=5, pady=5, side=LEFT)
        self.label4 = Label(self.row, width=3)
        self.label4.pack(side=LEFT, pady=5, padx=5)
        self.row.pack()

        self.clear_button = Button(self.top, text="Clear", command=self.clear, width=22).pack(padx=5, pady=5)

        self.letter1.trace("w", lambda name, index, mode, word1=self.letter1: self.parse())
        self.letter2.trace("w", lambda name, index, mode, word2=self.letter2: self.parse())
        self.letter3.trace("w", lambda name, index, mode, word3=self.letter3: self.parse())
        self.letter4.trace("w", lambda name, index, mode, word4=self.letter4: self.parse())
        self.letter5.trace("w", lambda name, index, mode, word5=self.letter5: self.parse())

    def parse(self):
        result1 = list()
        result2 = list()
        result3 = list()
        result4 = list()
        result5 = list()

        first = ''
        second = ''
        third = ''
        fourth = ''
        fifth = ''

        if self.letter1.get() is not None and self.morse_codes.__contains__(self.letter1.get()):
            first = self.decodes.get(self.letter1.get())
        if self.letter2.get() is not None and self.morse_codes.__contains__(self.letter2.get()):
            second = self.decodes.get(self.letter2.get())
        if self.letter3.get() is not None and self.morse_codes.__contains__(self.letter3.get()):
            third = self.decodes.get(self.letter3.get())
        if self.letter4.get() is not None and self.morse_codes.__contains__(self.letter4.get()):
            fourth = self.decodes.get(self.letter4.get())
        if self.letter5.get() is not None and self.morse_codes.__contains__(self.letter5.get()):
            fifth = self.decodes.get(self.letter5.get())

        for word in self.words:
            if first == word[0]:
                result1.append(word)
        for word in self.words:
            if second == word[1]:
                result2.append(word)
        for word in self.words:
            if third == word[2]:
                result3.append(word)
        for word in self.words:
            if fourth == word[3]:
                result4.append(word)
        for word in self.words:
            if fifth == word[4]:
                result5.append(word)

        final = list()

        if not self.morse_codes.__contains__(self.letter1.get()):
            letter1 = False
            self.label0.configure(text='error')
        else:
            letter1 = True
            self.label0.configure(text=first)
        if not self.morse_codes.__contains__(self.letter2.get()):
            letter2 = False
            self.label1.configure(text='error')
        else:
            letter2 = True
            self.label1.configure(text=second)
        if not self.morse_codes.__contains__(self.letter3.get()):
            letter3 = False
            self.label2.configure(text='error')
        else:
            letter3 = True
            self.label2.configure(text=third)
        if not self.morse_codes.__contains__(self.letter4.get()):
            letter4 = False
            self.label3.configure(text='error')
        else:
            letter4 = True
            self.label3.configure(text=fourth)
        if not self.morse_codes.__contains__(self.letter5.get()):
            letter5 = False
            self.label4.configure(text='error')
        else:
            letter5 = True
            self.label4.configure(text=fifth)

        final = self.words.copy()

        for i in range(len(self.words)):
            if letter1:
                if final.__contains__(self.words[i]):
                    if not result1.__contains__(self.words[i]):
                        final.pop(final.index(self.words[i]))


            if letter2:
                if not result2.__contains__(self.words[i]) and final.__contains__(self.words[i]):
                    final.pop(final.index(self.words[i]))
            if letter3:
                if not result3.__contains__(self.words[i]) and final.__contains__(self.words[i]):
                    final.pop(final.index(self.words[i]))
            if letter4:
                if not result4.__contains__(self.words[i]) and final.__contains__(self.words[i]):
                    final.pop(final.index(self.words[i]))
            if letter5:
                if not result5.__contains__(self.words[i]) and final.__contains__(self.words[i]):
                    final.pop(final.index(self.words[i]))

        super_final = list()
        for i in range(len(final)):
            super_final.append(self.words_frequencies.get(final[i]))

        for i in range(len(self.frequencies)):
            if super_final.__contains__(self.labels[i].cget("text")):
                self.labels[i].configure(bg="#a5ff8f")
            else:
                self.labels[i].configure(bg="#ffa6a6")

        result1.clear()
        result2.clear()
        result3.clear()
        result4.clear()

    def clear(self):
        self.input0.delete(0, END)
        self.input1.delete(0, END)
        self.input2.delete(0, END)
        self.input3.delete(0, END)
        self.input4.delete(0, END)
        self.label0.configure(text='')
        self.label1.configure(text='')
        self.label2.configure(text='')
        self.label3.configure(text='')
        self.label4.configure(text='')
        for i in range(len(self.frequencies)):
            self.labels[i].configure(bg="#ffa6a6")

