from tkinter import *
from tkinter import messagebox
import math


class Calc:
    def __init__(self) -> None:
        #window settings
        self.root = Tk()
        self.root.geometry("260x440")
        self.root.resizable(0,0)
        self.root.title("Azor_calc")
        self.background = Label(self.root, bg="white").place(x=0,y=0,relwidth=1,relheight=1)

        #entry
        self.entry = Entry(self.root, justify="right", font=("Terminal", 25), bg="#2d4870", fg="white")
        self.entry.place(x=0, y=0, width=260, height=100)
        
        #buttons
        ac = Button(self.root, text="AC", font=("Terminal", 20), command=self.clear_en, bg="white", fg="black").place(x=0, y=100, width=70, height=70)
        x2 = Button(self.root, text="x²", font=("Terminal", 20), command=self.kvadrat, bg="white", fg="black").place(x=65, y=100, width=70, height=70)
        koren = Button(self.root, text="√", font=("Terminal", 20), command=self.koren, bg="white", fg="black").place(x=130, y=100, width=70, height=70)
        divide = Button(self.root, text="÷", font=("Terminal", 20), command = lambda: self.but_entry('/'), bg="#ff7700", fg="white").place(x=195, y=100, width=70, height=70)
        num7 = Button(self.root, text="7", font=("Time", 20), command = lambda: self.but_entry('7'), bg="white", fg="black").place(x=0, y=168, width=68, height=70)
        num8 = Button(self.root, text="8", font=("Time", 20), command = lambda: self.but_entry('8'), bg="white", fg="black").place(x=65, y=168, width=68, height=70)
        num9 = Button(self.root, text="9", font=("Time", 20), command = lambda: self.but_entry('9'), bg="white", fg="black").place(x=130, y=168, width=68, height=70)
        multiply = Button(self.root, text="×", font=("Terminal", 20), command = lambda: self.but_entry('*'), bg="#ff7700", fg="white").place(x=195, y=168, width=68, height=70)
        num4 = Button(self.root, text="4", command = lambda: self.but_entry('4'), font=("Time", 20), bg="white", fg="black").place(x=0, y=235, width=68, height=70)
        num5 = Button(self.root, text="5", command = lambda: self.but_entry('5'), font=("Time", 20), bg="white", fg="black").place(x=65, y=235, width=68, height=70)
        num6 = Button(self.root, text="6", command = lambda: self.but_entry('6'), font=("Time", 20), bg="white", fg="black").place(x=130, y=235, width=68, height=70)
        minus = Button(self.root, text="-", font=("Time", 20), bg="#ff7700", command = lambda: self.but_entry('-'), fg="white").place(x=195, y=235, width=68, height=70)
        num1 = Button(self.root, text="1", command = lambda: self.but_entry('1'), font=("Time", 20), bg="white", fg="black").place(x=0, y=303, width=68, height=70)
        num2 = Button(self.root, text="2", command = lambda: self.but_entry('2'), font=("Time", 20), bg="white", fg="black").place(x=65, y=303, width=68, height=70)
        num3 = Button(self.root, text="3", command = lambda: self.but_entry('3'), font=("Time", 20), bg="white", fg="black").place(x=130, y=303, width=68, height=70)
        plus = Button(self.root, text="+", font=("Terminal", 20), command = lambda: self.but_entry('+'), bg="#ff7700", fg="white").place(x=195, y=303, width=68, height=70)
        num0 = Button(self.root, text="0", command = lambda: self.but_entry('0'), anchor="w",font=("Time", 20), bg="white", fg="black").place(x=0, y=371, width=133, height=70)
        dot = Button(self.root, text=".", font=("Time", 20), command = lambda: self.but_entry('.'), bg="white", fg="black").place(x=130, y=371, width=68, height=70)
        equal = Button(self.root, text="=", command=self.scanner_entry, font=("Time", 20), bg="#ff7700", fg="white").place(x=195, y=371, width=68, height=70)
        self.root.mainloop()

    #scanner of entry
    def scanner_entry(self):
        pass
        

    #entry of amount from button
    def but_entry(self, element):
        self.entry.insert(END, element)

    #clear ---> AC
    def clear_en(self):
        self.entry.delete(0, END)

    #kvadrat
    def kvadrat(self):
        if self.entry.get().isdigit():
            num = int(self.entry.get())**2
            self.entry.delete(0, END)
            self.entry.insert(END, str(num))
        else:
            messagebox.showerror("Error", "Enter only one number for calc and without space")

    def koren(self):
        if self.entry.get().isdigit():
            num = math.sqrt(int(self.entry.get()))
            self.entry.delete(0, END)
            self.entry.insert(END, "%.2f" % (num))
        else:
            messagebox.showerror("Error", "Enter only one number for calc and without space")

user = Calc()