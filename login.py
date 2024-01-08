import time
from tkinter import *
from tkinter import messagebox
import mysql.connector

import main
def logg():
    mydb=mysql.connector.connect(host="localhost",user="root",password="abohamza@2001",database="db1")

    # sql = "insert into password (password) values('mazen')"
    # newdb=mydb.cursor()
    # newdb.execute(sql)
    # mydb.commit()


    log = Tk()


    log.geometry('500x500')
    log.title('LOGIN')
    log.resizable(True,True)
    log.config(background="#D5DBDB")
    #title
    Label(log,text='تسجيل الدخول',font=('Courier',15),bg='black',fg='white').pack(fill=X)
    #fram
    fram1= Frame(log,width=300, height=350, bg='whitesmoke').pack(pady=30)
    #fram index

    Label(fram1, text='Password:', font=('Courier', 15), bg='whitesmoke', fg='black').place(x=100,y=150)
    def passw():
        x = var.get()
        sql = "select password from password"
        newdb = mydb.cursor()
        newdb.execute(sql)
        r = newdb.fetchone()
        if x==r[0]:
            log.destroy()
            main.fun()
        else:
            messagebox.showinfo("خطأ","خطأ في كلمة السر")
            log.destroy()
            logg()


    var=StringVar()
    en1 = Entry(fram1,width=30,textvariable=var).place(x=120,y=190)






    Button(fram1,width=10,text='دخول',fg="black",command=passw).place(x=120,y=300)










    log.mainloop()
logg()