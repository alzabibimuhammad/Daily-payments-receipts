import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime as d
from tkinter import messagebox
import change_pass

import mysql.connector

def fun():
    mydb=mysql.connector.connect(host="localhost",user="root",password="abohamza@2001",database="db1")
    x= str(d.datetime.today().date())
    print(x)
    cur= mydb.cursor()
    sql = "select  price , reason , id from sales where cast(date as date) = curdate()"

    cur.execute(sql)
    result = cur.fetchall()

    cur2= mydb.cursor()
    sql2 = 'select price , reason , id from receipts where cast(date as date) = curdate()'
    cur2.execute(sql2)
    result2 = cur2.fetchall()
    win = Tk()
    Label(win,fg="black",background='whitesmoke',text='مدفوعات').place(x=300,y=40)
    Label(win,fg="black",background='whitesmoke',text='مبيعات').place(x=900,y=40)
    frm = Frame(win)
    frm.pack(side=tk.LEFT,pady=1, padx=0)
    frm2 = Frame(win)
    frm2.pack(side=tk.LEFT, pady=10,padx=0)

    tv = ttk.Treeview(frm, columns=(1,2,3), show= "headings", height="30")
    tv.pack()
    tv.heading(1, text="المبلغ")
    tv.heading(2, text="السبب")
    tv.heading(3, text="رقم المبلغ")

    tv2 = ttk.Treeview(frm2, columns=(1,2,3), show= "headings", height="30")
    tv2.pack()
    tv2.heading(1,text="المبلغ")
    tv2.heading(2, text="السبب ")
    tv2.heading(3, text="رقم المبلغ")

    for i in result:
        tv2.insert('','end',values=i,)

    for i in result2:
        tv.insert('','end',values=i,)




    win.title("Custoner Data")
    win.resizable(False, True)
    win.geometry('1700x800')
    win.config(background='whitesmoke')
    #--------------------------------------------------------------------------------------------------------------------------
    #summmmmm
    sql3 = "select sum(price) from sales where cast(date as date) = curdate();"
    cur3 = mydb.cursor()
    cur3.execute(sql3)
    sum_of_sales = cur3.fetchone()
    print(sum_of_sales[0])

    sql4 = "select sum(price) from receipts where cast(date as date) = curdate()"
    cur4 = mydb.cursor()
    cur4.execute(sql4)
    sum_of_receipts= cur4.fetchone()
    print(sum_of_receipts[0])
    #--------------------------------------------------------------------------------------------------------------------------

    Label(frm,font=15,text=str(sum_of_receipts[0])).pack(padx=20)
    Label(frm,font=15,bg='white',text="المجموع :").place(x=105,y=625)

    Label(frm2,font=15,text=str(sum_of_sales[0])).pack(padx=20)
    Label(frm2,font=15,bg='white',text="المجموع :").place(x=105,y=625)




    def change_password():
        win.destroy()
        change_pass.fun2()
    Button(win,text='change password',command=change_password).place(x=1595,y=30)
    #----------------------------------------------------------------------------
    #insert

    # --------------------------------------------------------------------------------------------

    def delete_sales():
        if id1.get():
            sql5="delete from sales where id = '"+id1.get()+"'"
            cur5 = mydb.cursor()
            cur5.execute(sql5)
            mydb.commit()
            win.destroy()
            fun()
        else:
            messagebox.showinfo("خطأ","أدخل رقم مبيع لحذفه ")


            pass
    def delete_receipts():
        if id12.get():
            sql6="delete from receipts where id = '"+id12.get()+"'"
            cur6 = mydb.cursor()
            cur6.execute(sql6)
            mydb.commit()
            win.destroy()
            fun()
        else:
            messagebox.showinfo("خطأ","أدخل رقم مدفوع لحذفه ")


    id1=StringVar()
    Label(win,text=" :أدخل رقم المبلغ لحذف مبيعات",font=10).place(x=1530,y=120)
    Entry(win,width=15,textvariable=id1,bg='white',font=10,fg='black').place(x=1380,y=120)
    Button(win,text='احذف',command=delete_sales).place(x=1330,y=120)

    id12=StringVar()
    Label(win,text=" :أدخل رقم المبلغ لحذف مدفوعات",font=10).place(x=1530,y=350)
    Entry(win,width=15,textvariable=id12,bg='white',font=10,fg='black').place(x=1380,y=350)
    Button(win,text='احذف',command=delete_receipts).place(x=1330,y=350)

#--------------------------------------------------------------------------------------------
    var0 = StringVar()
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()


    Label(win,text=" :أدخل مبيعات",font=10).place(x=1600,y=170)
    Entry(win,width=15,textvariable=var0,bg='white',font=10,fg='black').place(x=1450,y=170)
    Entry(win,width=15,textvariable=var1,font=10,bg='white',fg='black').place(x=1300,y=170)

    Label(win,text=" :أدخل مدفوعات",font=10).place(x=1600,y=300)
    Entry(win,width=15,textvariable=var2,font=10,bg='white',fg='black').place(x=1450,y=300)
    Entry(win,width=15,textvariable=var3,font=10,bg='white',fg='black').place(x=1300,y=300)

    def insert_sales():
        reason = var0.get()
        price= var1.get()
        if reason and price:
            sql7 = "insert into sales (reason,price) values('"+reason+"','"+price+"')"
            cur7 = mydb.cursor()
            cur7.execute(sql7)
            mydb.commit()
            win.destroy()
            fun()
        else:
            messagebox.showinfo("خطأ","أدخل جميع الحقول")


    def insert_receipts():
        reason = var2.get()
        price= var3.get()
        if reason and price:
            sql8 = "insert into receipts (reason,price) values('"+reason+"','"+price+"')"
            cur8 = mydb.cursor()
            cur8.execute(sql8)
            mydb.commit()
            win.destroy()
            fun()
        else:
            messagebox.showinfo("خطأ","أدخل جميع الحقول")


    Button(win,text='أدخل',command=insert_sales).place(x=1250,y=170)

    Button(win,text='أدخل',command=insert_receipts).place(x=1250,y=300)


    win.mainloop()
    pass

fun()