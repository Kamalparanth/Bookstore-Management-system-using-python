from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os
py=sys.executable

class operation(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(1366, 768)
        self.minsize(1366, 768)
        self.state("zoomed")
        self.title("e-book store")
        self.configure(background='orange')

        def des():
            self.destroy()
        def search():
            os.system('%s %s' % (py, 'search.py'))
        def review():
            os.system('%s %s' % (py, 'review.py'))
        def buy():
            os.system('%s %s' % (py, 'buy.py'))
             

        self.label =Label(self,text= "Welcome to e-book store",font=("Algerian",40,'bold'),fg='Green',bg='orange')
        self.label.place(x=330, y=75)
        self.butt  = Button(self, text="Search Book", font=30, height=3,width=20,fg='Blue',bg='White',command=search).place(x=600, y=200)
        self.butt2 = Button(self, text="Buy Book", font=30, height=3,width=20,fg='Blue',bg='white',command=buy).place(x=600, y=300)
        self.butt3 = Button(self, text="Review Book",font=30,height=3,width=20,fg='Blue',bg='white',command=review).place(x=600,y=400)
        self.butt4 = Button(self, text="Logout",font=30,height=3,width=20,fg='Blue',bg='white',command=des).place(x=600,y=500) 

        
                    
                    

operation().mainloop()
        
