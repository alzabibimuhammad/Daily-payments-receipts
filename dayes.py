from tkinter import *
import time
# import mysql.connector 

#mydb=mysql.connector.connect(host="localhost",user="root",password="abohamza@2001",database="db1")

# log=Tk()
# log.resizable('1980x1080')


# log.mainloop()


from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('dayes')
ws['bg']='#ffbf00'


 
def nextPage():
    ws.destroy()
    import page3
    


x=Button(
    ws, 
    text="Previous Page", 
    
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)



ws.mainloop()