import time
from tkinter import *
import mysql.connector
import main
def fun2():
    mydb=mysql.connector.connect(host="localhost",user="root",password="abohamza@2001",database="db1")

    # sql = "insert into password (password) values('mazen')"
    # newdb=mydb.cursor()
    # newdb.execute(sql)
    # mydb.commit()


    log = Tk()

    log.geometry('500x500')
    log.title('Change password')
    log.resizable(True,True)
    log.config(background="#D5DBDB")
    #title
    Label(log,text='تسجيل الدخول',font=('Courier',15),bg='black',fg='white').pack(fill=X)
    #fram
    fram1= Frame(log,width=300, height=350, bg='whitesmoke').pack(pady=30)
    #fram index
    Label(fram1, text='Old Password:', font=('Courier', 15), bg='whitesmoke', fg='black').place(x=100,y=150)
    Label(fram1, text='New Password:', font=('Courier', 15), bg='whitesmoke', fg='black').place(x=100,y=180)
    old=StringVar()
    new=StringVar()

    en1 = Entry(fram1,width=20,textvariable=old).place(x=260,y=150)
    en2 = Entry(fram1,width=20,textvariable=new).place(x=260,y=180)




    def passw():
        x = old.get()
        y = new.get()
        sql = "select password from password"
        newdb = mydb.cursor()
        newdb.execute(sql)
        r = newdb.fetchone()
        if x==r[0]:
            sql = "update password set password = '"+y+"'"
            newdb.execute(sql)
            mydb.commit()
            log.destroy()
            main.fun()
        else:
            x = Message(fram1,text='خطأ في كلمة السر', bg='red',fg='black').pack()

    def back():
        log.destroy()
        main.fun()

    Button(fram1,width=10,text='دخول',fg="black",command=passw).place(x=120,y=300)

    Button(fram1,width=10,text='رجوع',fg="black",command=back).place(x=300,y=300)

    log.mainloop()
