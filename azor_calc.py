from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from tkinter import font


class Calc:
    def __init__(self) -> None:
        #window settings
        self.root = Tk()
        self.root.geometry("400x400")
        self.root.resizable(0,0)
        self.root.title("Azor_calc")
        self.background = Label(self.root, bg="white").place(x=0,y=0,relwidth=1,relheight=1)

        #entry
        # self.entry = Entry(self.root,  bg="#E7E6E6")
        # self.entry.place(x=0,y=0,width=350,height=35)
        self.entry = Entry(self.root, justify="right", font=("Terminal", 35), bg="#20569e", fg="white").place(x=0, y=0, width=400, height=100)


        self.root.mainloop()

user = Calc()