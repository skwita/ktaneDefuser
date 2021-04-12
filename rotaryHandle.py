from tkinter import *


class RotaryHandle:
    def __init__(self, master):
        self.top = Toplevel(master)
        self.top.title('Поворотная ручка')
        self.frame = Frame(self.top)

        self.var1 = BooleanVar()
        self.var2 = BooleanVar()
        self.var3 = BooleanVar()
        self.var4 = BooleanVar()
        self.var5 = BooleanVar()
        self.var6 = BooleanVar()
        self.var7 = BooleanVar()
        self.var8 = BooleanVar()
        self.var9 = BooleanVar()
        self.var10 = BooleanVar()
        self.var11 = BooleanVar()
        self.var12 = BooleanVar()

        self.row0 = Frame(self.top)
        Checkbutton(self.row0, variable=self.var1, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Checkbutton(self.row0, variable=self.var2, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Checkbutton(self.row0, variable=self.var3, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Checkbutton(self.row0, variable=self.var4, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Checkbutton(self.row0, variable=self.var5, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Checkbutton(self.row0, variable=self.var6, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        self.row0.pack()

        self.row1 = Frame(self.top)
        Checkbutton(self.row1, variable=self.var7, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Checkbutton(self.row1, variable=self.var8, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Checkbutton(self.row1, variable=self.var9, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Checkbutton(self.row1, variable=self.var10, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Checkbutton(self.row1, variable=self.var11, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        Checkbutton(self.row1, variable=self.var12, width=1, onvalue=1, offvalue=0).pack(side=LEFT)
        self.row1.pack()

        self.row2 = Frame(self.top)
        Button(self.row2, text='click', command=self.proceed).pack(side=LEFT, padx=5, pady=5)
        Button(self.row2, text='clear', command=self.clear).pack(side=LEFT, padx=5, pady=5)
        self.row2.pack()

        self.lbl = Label(self.top)
        self.lbl.pack()

    def proceed(self):
        if not self.var1.get() and not self.var2.get() and self.var3.get()\
                and not self.var4.get() and self.var5.get() and self.var6.get()\
                and self.var7.get() and self.var8.get() and self.var9.get()\
                and self.var10.get() and not self.var11.get() and self.var12.get() or\
                self.var1.get() and not self.var2.get() and self.var3.get()\
                and not self.var4.get() and self.var5.get() and not self.var6.get()\
                and not self.var7.get() and self.var8.get() and self.var9.get()\
                and not self.var10.get() and self.var11.get() and self.var12.get():
            self.lbl.configure(text="вверх")
        elif not self.var1.get() and self.var2.get() and self.var3.get()\
                and not self.var4.get() and not self.var5.get() and self.var6.get()\
                and self.var7.get() and self.var8.get() and self.var9.get()\
                and self.var10.get() and not self.var11.get() and self.var12.get() or\
                self.var1.get() and not self.var2.get() and self.var3.get()\
                and not self.var4.get() and self.var5.get() and not self.var6.get()\
                and not self.var7.get() and self.var8.get() and not self.var9.get()\
                and not self.var10.get() and not self.var11.get() and self.var12.get():
            self.lbl.configure(text="вниз")
        elif not self.var1.get() and not self.var2.get() and not self.var3.get()\
                and not self.var4.get() and self.var5.get() and not self.var6.get()\
                and self.var7.get() and not self.var8.get() and not self.var9.get()\
                and self.var10.get() and self.var11.get() and self.var12.get() or\
                not self.var1.get() and not self.var2.get() and not self.var3.get()\
                and not self.var4.get() and self.var5.get() and not self.var6.get()\
                and not self.var7.get() and not self.var8.get() and not self.var9.get()\
                and self.var10.get() and self.var11.get() and not self.var12.get():
            self.lbl.configure(text="влево")
        elif self.var1.get() and not self.var2.get() and self.var3.get()\
                and self.var4.get() and self.var5.get() and self.var6.get()\
                and self.var7.get() and self.var8.get() and self.var9.get()\
                and not self.var10.get() and self.var11.get() and not self.var12.get() or\
                self.var1.get() and not self.var2.get() and self.var3.get()\
                and self.var4.get() and not self.var5.get() and not self.var6.get()\
                and self.var7.get() and self.var8.get() and self.var9.get()\
                and not self.var10.get() and self.var11.get() and not self.var12.get():
            self.lbl.configure(text="вправо")
        else:
            self.lbl.configure(text="Какой же ты все-таки тупой....")


    def clear(self):
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)
        self.var9.set(0)
        self.var10.set(0)
        self.var11.set(0)
        self.var12.set(0)


