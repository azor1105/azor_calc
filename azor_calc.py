from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from tkinter import font


class Calc:
    def __init__(self) -> None:
        #window settings
        self.root = Tk()
        self.root.geometry("260x450")
        self.root.resizable(0,0)
        self.root.title("Azor_calc")
        self.background = Label(self.root, bg="white").place(x=0,y=0,relwidth=1,relheight=1)

        #entry
        self.entry = Entry(self.root, justify="right", font=("Terminal", 25), bg="#2d4870", fg="white").place(x=0, y=0, width=260, height=100)

        #buttons
        ac = Button(self.root, text="AC", font=("Terminal", 20), bg="white", fg="black").place(x=0, y=100, width=70, height=70)
        x2 = Button(self.root, text="x²", font=("Terminal", 20), bg="white", fg="black").place(x=65, y=100, width=70, height=70)
        koren = Button(self.root, text="√", font=("Terminal", 20), bg="white", fg="black").place(x=130, y=100, width=70, height=70)
        divide = Button(self.root, text="÷", font=("Terminal", 20), bg="#ff7700", fg="white").place(x=195, y=100, width=70, height=70)
        num7 = Button(self.root, text="7", font=("Time", 20), bg="white", fg="black").place(x=0, y=168, width=68, height=70)
        num8 = Button(self.root, text="8", font=("Time", 20), bg="white", fg="black").place(x=65, y=168, width=68, height=70)
        num9 = Button(self.root, text="9", font=("Time", 20), bg="white", fg="black").place(x=130, y=168, width=68, height=70)
        multiply = Button(self.root, text="×", font=("Terminal", 20), bg="#ff7700", fg="white").place(x=195, y=168, width=68, height=70)
        num4 = Button(self.root, text="4", font=("Time", 20), bg="white", fg="black").place(x=0, y=235, width=68, height=70)
        num5 = Button(self.root, text="5", font=("Time", 20), bg="white", fg="black").place(x=65, y=235, width=68, height=70)
        num6 = Button(self.root, text="6", font=("Time", 20), bg="white", fg="black").place(x=130, y=235, width=68, height=70)
        minus = Button(self.root, text="-", font=("Time", 20), bg="#ff7700", fg="white").place(x=195, y=235, width=68, height=70)
        self.root.mainloop()

user = Calc()