from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width


class Calc:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.resizable(0,0)
        self.root.title("Azor_calc")

        self.background = Label(self.root, bg="white").place(x=0,y=0,relwidth=1,relheight=1)
        self.root.mainloop()

user = Calc()