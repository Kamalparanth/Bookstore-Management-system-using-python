from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os
py=sys.executable

class Book(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(1366, 768)
        self.minsize(1366, 768)
        self.state("zoomed")
        self.title("e-book store")
 

        def login():
                if len(self.user_text.get()) < 0:
                    messagebox.showinfo("Oop's","Please Enter Your Username")
                elif len(self.pass_text.get()) < 0:
                    messagebox.showinfo("Oop's","Please Enter Your Password")
                else:
                    try:
                       self.conn = sqlite3.connect('Bookstore.db')
                       self.myCursor = self.conn.cursor()
                       self.myCursor.execute("Select * from User_login where username=? AND password =?",[self.user_text.get(),self.pass_text.get()])
                       self.pc = self.myCursor.fetchall()
                       self.myCursor.close()
                       self.conn.close()
                       if self.pc:
                            self.destroy()
                            os.system('%s %s' % (py, 'operations.py'))
                       else:
                           messagebox.showinfo('Error', 'Username and password not found')
                           self.user_text.delete(0, END)
                           self.pass_text.delete(0, END)
                    except Error:
                       messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")
                       
        def forgotpassword():
                os.system('%s %s' % (py, 'forgotpassword.py'))

        def signup():
                os.system('%s %s' % (py, 'signup.py'))


        self.label =Label(self,text= "Welcome to e-book world !!!",font=("Algerian",40,'bold'),fg='Green')
        self.label.place(x=230, y=10)
        self.label = Label(self, text=" USER Login ", font=("Algerian", 30, 'bold'))
        self.label.place(x=500, y=100)
        self.label1 = Label(self, text="Username:", font=("Times New roman", 25, 'bold'))
        self.label1.place(x=350, y=250)
        self.user_text = Entry(self, textvariable=self.a, width=50)
        self.user_text.place(x=525, y=265)
        self.label2 = Label(self, text="Password:", font=("Times new roman", 25, 'bold'))
        self.label2.place(x=350, y=300)
        self.pass_text = Entry(self, show='*', textvariable=self.b, width=50)
        self.pass_text.place(x=525, y=315)
        self.butt  = Button(self, text="Login", font=10, width=15,fg='Blue',bg='White',command=login).place(x=350, y=400)
        self.butt2 = Button(self, text="Forgot Password", font=10, width=15,fg='Blue',bg='white',command=forgotpassword).place(x=600, y=400)
        self.butt3 = Button(self, text="Signup",font=10,width=15,fg='Blue',bg='white',command=signup).place(x=850,y=400)
        
Book().mainloop()
        
