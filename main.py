from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from curses.ascii import isalnum

class Regist:
    def __init__(self,root):
        #list for scanning data of user
        self.baza = []
        #properety for ckecking password
        self.joy = None
        self.saqlagich = None
        #property for changing pass andm login
        self.ishora = None
        #settings
        self.root = root
        self.root.title("Sign in")
        self.root.geometry("960x720")
        self.root.resizable(False,False)
        #starting collecting data
        self.get_info()
        

        #backgroud
        self.bg = PhotoImage(file= ".A'zamboy korporeyshn.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #window an wallpaper
        Frame_login = Frame(self.root,bg="white")
        Frame_login.place(x=100,y=70,width=750,height=570)

        #title
        title = Label(Frame_login, text="Sign in", font=("Goudy old style", 36, "bold"), fg="black",bg="white").place(x=300,y=30)

        #nick
        user = Label(Frame_login, text="Login", font=("Goudy old style", 20, "bold"), fg="grey",bg="white").place(x=150,y=140)
        self.nick = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.nick.place(x=150,y=190,width=350,height=35)

        #pass
        parol = Label(Frame_login, text="Password", font=("Goudy old style", 20, "bold"), fg="grey",bg="white").place(x=150,y=240)
        self.password = Entry(Frame_login, show = '*', font = ("Goudy old style", 20, "bold"), bg="#E7E6E6")
        self.password.place(x=150,y=280,width=350,height=35)

        #button forget && submit && exit
        forget = Button(Frame_login, text="Do you forgot?", bd=0, cursor="hand2", command=self.mess,font=("Goudy old style", 15), fg="black", bg="white").place(x=150,y=330, width=150,height=25)
        submit = Button(Frame_login, text="Submit", cursor="hand2", command=lambda:[self.tester(),self.check()], font=("Goudy old style", 20, "bold"), fg="blue", bg="white").place(x=150,y=370)
        exit = Button(Frame_login, text="Exit", cursor="hand2", command=root.destroy, font=("Terminal", 20),fg="black",bg="white").place(x=620,y=450)
        regitstrate = Button(Frame_login, text="Sign up", cursor="hand2", command=self.sign_up,font=("ar 15 bold"),fg="black",bg="white").place(x=610,y=520)

    #method not closable window
    def nothing(self):
        pass

    #check in field in loginning
    def check(self):
        if self.password.get() == "" and self.nick.get() == "":
            messagebox.showerror("Error", "All fields is empty", parent=self.root)
        elif self.joy == None:
            messagebox.showerror("Error", "Password or login is wrong", parent=self.root)
        else:
            self.saqlagich = self.joy
            self.joy = None
            self.mal()


    #sign up window for future or new users
    def sign_up(self):
        #settings
        self.sign_up_win = Tk()
        self.sign_up_win.title("Sign up")
        self.sign_up_win.geometry("560x420")
        self.sign_up_win.resizable(False,False)
        
        #cleaning
        self.password.delete(0, END)
        self.nick.delete(0, END)
        
        #label and buttons
        up_label = Label(self.sign_up_win, text="Sign up", font=("ar 20 bold"), fg="black").place(x=220,y=20)
        
        #age
        age_label = Label(self.sign_up_win, text="Age", font=("ar 18 bold"), fg="black").place(x=50,y=70)
        self.age_entry = Entry(self.sign_up_win, font=("ar 15"), fg="black", bg="#E7E6E6")
        self.age_entry.place(x=120,y=70,width=50,height=35)
        
        #login
        user_label = Label(self.sign_up_win, text="Login", font=("Goudy old style", 18, "bold"), fg="black").place(x=50,y=120)
        self.new_login = Entry(self.sign_up_win, font=("Goudy old style", 15), bg="#E7E6E6")
        self.new_login.place(x=150,y=120,width=250,height=35)
        
        #enter pass
        password_label = Label(self.sign_up_win, text="Enter password", font=("Goudy old style", 15, "bold"), fg="black").place(x=50,y=175)
        self.up_password = Entry(self.sign_up_win, show="*", font=("Goudy old style", 20), bg="#E7E6E6")
        self.up_password.place(x=240, y=170, width=300,height=35)

        #confirm pass
        confirm_password_label = Label(self.sign_up_win, text="Confirm password", font=("Goudy old style", 13, "bold"), fg="black").place(x=50,y=245)
        self.con_up_password = Entry(self.sign_up_win, show="*", font=("Goudy old style", 20), bg="#E7E6E6")
        self.con_up_password.place(x=240, y=240, width=300,height=35)
        
        #buttons ok && cancel
        up_ok = Button(self.sign_up_win, text="ok", cursor="hand2", command=self.up_check, font=("ar 18 bold"),fg="black").place(x=50,y=340)
        up_cancel = Button(self.sign_up_win, text="cancel", cursor="hand2", command=self.sign_up_win.destroy,font=("ar 15 bold"), fg="black").place(x=440,y=345)
        self.sign_up_win.mainloop()
    
    #check fields in sign up
    def up_check(self):
        if self.age_entry.get() == "" or self.new_login.get() == "" or self.up_password.get() == "" or self.con_up_password.get() == "":
            messagebox.showerror("Error", "Field is empty", parent=self.sign_up_win) 
        elif self.age_entry.get()[0] == "0":
            messagebox.showerror("Error", "Invalid age", parent=self.sign_up_win)
        elif int(self.age_entry.get()) > 100:
            messagebox.showerror("Error", "Max age is 100", parent=self.sign_up_win)
        elif int(self.age_entry.get()) <= 15:
            messagebox.showinfo("Info", "Sorry this application is 16+", parent=self.sign_up_win) 
        elif len(self.new_login.get()) <= 2:
            messagebox.showerror("Error", "Login must be more then 2 symbols", parent=self.sign_up_win)
        elif self.new_login.get().isalnum() != True:
            messagebox.showerror("Error", "Invalid login", parent=self.sign_up_win)
        elif self.new_login.get().islower() != True:
            messagebox.showerror("Error", "Login must be lower case", parent=self.sign_up_win) 
        elif self.helper_scan_new_login():
            messagebox.showerror("Error", "This login is busy", parent=self.sign_up_win)
        elif self.up_password.get() != self.con_up_password.get():
            messagebox.showerror("Error", "Plese enter the similar password", parent=self.sign_up_win)
        elif len(self.up_password.get()) < 6:
            messagebox.showerror("Error", "Length of pasword must be min 6", parent=self.sign_up_win)
        else:
            with open(".info.txt", "a") as f:
                f.write("\nlogin="+self.new_login.get()+"|"+"pass="+self.con_up_password.get())
            self.baza.clear()
            self.get_info()
            messagebox.showinfo("Info", "You have succesfully registrated", parent=self.sign_up_win)
            self.sign_up_win.destroy()


    #message in button "forgot password"
    def mess(self):
        messagebox.showinfo("Info","Man qattan bilaman")
    
    #window after signing --> password, login, del account
    def mal(self):
        #settings
        self.mirror = Tk()
        self.mirror.title("Hi")
        self.mirror.geometry("390x300")
        self.mirror.resizable(False,False)
        self.mirror.protocol("WM_DELETE_WINDOW", self.nothing)
        
        #label and button 
        title = Label(self.mirror, text=f"Welcome {self.nick.get()}", font=("Goudy old style", 13, "bold"), fg="black").place(x=120,y=10)
        title = Label(self.mirror, text=f"What do you want to change", font=("Goudy old style", 12, "bold"), fg="black").place(x=60,y=50)
        tanla_pass = Button(self.mirror, text="Password", command=self.change, cursor = "hand2", font=("Goudy old style", 13, "bold"), fg= "black").place(x=120, y=90)
        tanla_login = Button(self.mirror, text="Login", cursor="hand2", command=self.login_change,font=("Goudy old style", 13, "bold"), fg= "black").place(x=140, y=140)
        tanla_login_ochir = Button(self.mirror, text="Del account", cursor="hand2", command=self.ogohlantir, font=("Goudy old style", 13, "bold"), fg= "black").place(x=110, y=190)
        close = Button(self.mirror, text="log out", cursor="hand2", command=self.tozala, font=("Time", 13), fg="black").place(x=280, y=240)
        self.mirror.mainloop()
    
    #func log_out button clear
    def tozala(self):
        self.password.delete(0, END)
        self.nick.delete(0, END)
        self.mirror.destroy()

    #cancel button clear
    def mohir_pass(self):
        self.passworde.destroy()
        self.mal()

    def mohir_login(self):
        self.win_login.destroy()
        self.mal()

    def mohir_no(self):
        self.yes_no.destroy()
        self.mal()

    #password change
    def change(self):
        #closing self.mirror --> password, login, del account
        self.mirror.destroy()

        #settings of "change"
        self.passworde = Tk()
        self.passworde.title("Password")
        self.passworde.geometry("650x400")
        self.passworde.resizable(False,False)
        self.passworde.protocol("WM_DELETE_WINDOW", self.nothing)
    
        #title enter password
        title_password = Label(self.passworde, text="Enter new password", font=("Goudy old style", 20, "bold"), fg="black").place(x=40,y=10)
        self.entry_password = Entry(self.passworde, show="*", font=("Goudy old style", 20), bg="#E7E6E6")
        self.entry_password.place(x=40, y=60, width=400,height=35)
        
        #title confirm password
        title_confirm = Label(self.passworde, text="Confirm password", font=("Goudy old style", 20, "bold"), fg="black").place(x=40,y=120)
        self.confirm_password = Entry(self.passworde, show="*", font=("Goudy old style", 20), bg="#E7E6E6")
        self.confirm_password.place(x=40, y=170, width=400,height=35)

        #button confirm
        ok = Button(self.passworde, text="Ok", command=self.scan, cursor="hand2", font=("Goudy old style", 20, "bold")).place(x=40, y=250)
        cancel = Button(self.passworde, text="cancel", command=self.mohir_pass, cursor="hand2", font=("Goudy old style", 15, "bold")).place(x=510, y=320)
        self.passworde.mainloop()

    # checking entry of new password
    def scan(self):
        #for knowing changing of password in function --> almashtir()
        self.ishora = True
        if self.entry_password.get() == "" and self.confirm_password.get() == "":
            messagebox.showerror("Error", "All fields is empty", parent=self.password)
        elif self.entry_password.get() == self.saqlagich["pass"] and self.confirm_password.get() == self.saqlagich["pass"]:
            messagebox.showerror("Error", "Enter new password not old", parent=self.password)
        elif self.entry_password.get() != self.confirm_password.get():
            messagebox.showerror("Error", "Please enter the same password to all fields", parent=self.password)
        elif len(self.confirm_password.get()) < 6:
            messagebox.showerror("Error", "Please enter more symbols than 5", parent=self.password)
        else:
            self.almashtir()  
            messagebox.showinfo("Info", "Password has succesfully changed", parent=self.password)
            self.passworde.destroy()
            self.baza.clear()
            self.get_info()
            self.password.delete(0, END)
            self.nick.delete(0, END)
            #self.root.destroy()

    #login change
    def login_change(self):
        #closing self.mirror --> password, login, del account
        self.mirror.destroy()
        #settings
        self.win_login = Tk()
        self.win_login.title("Login")
        self.win_login.geometry("300x250")
        self.win_login.resizable(False,False)
        self.win_login.protocol("WM_DELETE_WINDOW", self.nothing)
        #label and button
        nomi = Label(self.win_login, text="Enter new login", font=("Goudy old style", 20, "bold"), fg="black").place(x=35,y=10)
        self.new_login = Entry(self.win_login, font=("Goudy old style", 20), bg="#E7E6E6")
        self.new_login.place(x=35, y=80, width=230,height=35)
        boldi = Button(self.win_login, text="Ok", command=self.scan_new_login, font=("Goudy old style", 13, "bold"), fg="black").place(x=35,y=180)
        boldmadi = Button(self.win_login, text="cancel", command=self.mohir_login, font=("Goudy old style", 12, "bold"), fg="black").place(x=200,y=190)

    #scanning the self.new_login part1
    def scan_new_login(self):
        if self.new_login.get() == "":
            messagebox.showerror("Error", "Field is empty", parent=self.win_login)
        elif self.nick.get() == self.new_login.get():
            messagebox.showerror("Error", "Enter new login not old", parent=self.win_login)
        elif len(self.new_login.get()) <= 2:
            messagebox.showerror("Error", "Login must be more then 2 symbols", parent=self.win_login)
        elif self.new_login.get().isalnum() != True or self.new_login.get().isnumeric() == True:
            messagebox.showerror("Error", "Invalid login", parent=self.win_login)
        elif self.new_login.get().islower() != True:
            messagebox.showerror("Error", "Login must be lower case", parent=self.win_login)
        elif self.helper_scan_new_login():
            messagebox.showerror("Error", "This login is busy", parent=self.win_login)
        else:
            self.ishora = False
            self.almashtir()
            messagebox.showinfo("Info", "Login has succesfully changed", parent=self.win_login)
            self.win_login.destroy()
            self.baza.clear()
            self.get_info()
            self.password.delete(0, END)
            self.nick.delete(0, END)
            #self.root.destroy()
    
    #conntinuing part2
    def helper_scan_new_login(self):
        for line in self.baza:
            if self.new_login.get() == line["login"]:
                return True
        return False

    #data of users
    def get_info(self):
        with open(".info.txt") as f:
            info = f.read()

        for qator in info.split():
            self.baza.append(
                {
                    "login": qator.split("|")[0].split("=")[1],
                    "pass": qator.split("|")[1].split("=")[1],
                }
            )


    #aunthefication login and pass
    def tester(self):
        for joy in self.baza:
            if self.password.get() == joy["pass"] and self.nick.get() == joy["login"]:
                self.joy = joy
            

    #changin password and login
    def almashtir(self):
        #True --> for changing password
        if self.ishora == True:
            # opening the file in read mode
            file = open(".info.txt", "r")
            replacement = ""
            # using the for loop
            for line in file:
                line = line.strip()
                changes = line.replace("login="+self.saqlagich["login"] + "|" + "pass="+self.saqlagich["pass"], "login="+self.saqlagich["login"] + "|" + "pass="+self.entry_password.get())
                replacement = replacement + changes + "\n"
            file.close()
            # opening the file in write mode
            fout = open(".info.txt", "w")
            fout.write(replacement)
            fout.close() 
            self.ishora = None
        #False --> for changing login
        elif self.ishora == False:
            # opening the file in read mode
            file = open(".info.txt", "r")
            replacement = ""
            # using the for loop
            for line in file:
                line = line.strip()
                changes = line.replace("login="+self.saqlagich["login"], "login="+self.new_login.get())
                replacement = replacement + changes + "\n"
            file.close()
            # opening the file in write mode
            fout = open(".info.txt", "w")
            fout.write(replacement)
            fout.close() 
            self.ishora = None
        #None --> deleting account
        else:
            # opening the file in read mode
            file = open(".info.txt", "r")
            replacement = ""
            # using the for loop
            for line in file:
                line = line.strip()
                changes = line.replace("login="+self.saqlagich["login"] + "|" + "pass="+self.saqlagich["pass"], "")
                replacement = replacement + changes + "\n"
            file.close()
            # opening the file in write mode
            fout = open(".info.txt", "w")
            fout.write(replacement)
            fout.close()
            messagebox.showinfo("Info", "Your account has been deleted", parent=self.yes_no)
            self.yes_no.destroy()
            self.baza.clear()
            self.get_info()
            self.password.delete(0, END)
            self.nick.delete(0, END)
            #self.root.destroy()


    #window in deleting account
    def ogohlantir(self):
        self.mirror.destroy()
        self.yes_no = Tk()
        self.yes_no.title("Sure")
        frm = ttk.Frame(self.yes_no, padding=100)
        frm.grid()
        self.yes_no.resizable(False,False)
        self.yes_no.protocol("WM_DELETE_WINDOW", self.nothing)
        ttk.Label(frm, text="Are you sure?", font="bold").grid(column=0, row=0)
        ttk.Button(frm, text="No", command=self.mohir_no).grid(column=0, row=1)
        ttk.Button(frm, text="Yes", command=self.almashtir).grid(column=0, row=2)
        self.yes_no.mainloop()

root = Tk()
obj = Regist(root)
root.mainloop()