from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error


class review(Tk):
    def __init__(self):
        super().__init__()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        z = StringVar()
        x = StringVar()
        self.title("Rate Book")
        self.maxsize(600,600)
        self.minsize(600,600)
    
        l1=Label(self,text="Rate Book",font=("Algerian",20,'bold')).place(x=200,y=20)
        
        def ins():
                try:
                    self.conn = sqlite3.connect('Bookstore.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Update Sales_Details set rating = ? where invoice_no = ?",[x.get(),b.get()])
                    self.conn.commit()
                    self.myCursor.close()
                    self.conn.close()
                    messagebox.showinfo("Confirm","Rating Updated Successfuly")
                    self.destroy()
                except Error:
                    messagebox.showerror("Error","Something Goes Wrong")

        def check():
            if len(a.get())== 0:
                messagebox.showinfo("Error","Please Enter Username")
            elif len(b.get()) == 0:
                messagebox.showinfo("Error","Please Enter invoice")
            elif len(c.get()) == 0:
                messagebox.showinfo("Error", "Please Enter a Book name")
            else:
                try:
                    self.conn = sqlite3.connect('Bookstore.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Select u_name,invoice_no,B_name from Sales_Details where u_name = ? and B_name = ? ",[a.get(),c.get()])
                    pc = self.myCursor.fetchone()
                    if not pc:
                        messagebox.showinfo("Error", "Something Wrong in the Details")
                    elif str(pc[0]) == a.get() or str(pc[3]) == b.get() or str(pc[2]) == c.get():
                        Label(self, text="Rating",font=('arial', 15, 'bold')).place(x=40, y= 320)
                        z=ttk.Combobox(self,textvariable=x,values=["1","2","3","4","5"],width=40,state="readonly").place(x = 250, y = 320)
                        Button(self, text="Submit", width=15, command=ins).place(x=250, y=350)
                except Error:
                    messagebox.showerror("Error","Something Goes Wrong")

        #label and input box
        Label(self, text="Enter username", font=('arial', 15, 'bold')).place(x=40, y=100)
        Label(self, text="Enter invoice number",font=('arial', 15, 'bold')).place(x=40, y= 150)
        Label(self, text="Enter Book name",font=('arial', 15, 'bold')).place(x=40, y= 200)
        Entry(self, textvariable=a, width=40).place(x=250, y=110)
        Entry(self, textvariable=b, width=40).place(x=250, y=160)
        Entry(self, textvariable=c, width=40).place(x=250, y=210)
        Button(self, text='Verify', width=15,command = check).place(x=250, y=270)                      
              

review().mainloop()


