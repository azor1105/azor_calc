from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from tkinter import font


class Calc:
    def __init__(self) -> None:
        #window settings
        self.root = Tk()
        self.root.geometry("300x450")
        self.root.resizable(0,0)
        self.root.title("Azor_calc")
        self.background = Label(self.root, bg="white").place(x=0,y=0,relwidth=1,relheight=1)

        #entry
        self.entry = Entry(self.root, justify="right", font=("Terminal", 35), bg="#2d4870", fg="white").place(x=0, y=0, width=300, height=100)

        #buttons
        ac = Button(self.root, text="AC", font=("Terminal", 20), bg="white", fg="black").place(x=0, y=100, width=70, height=70)

        self.root.mainloop()

user = Calc()