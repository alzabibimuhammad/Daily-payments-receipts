from tkinter import *

ws=Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg']='#ffbf00'

def nextPage():
    ws.destroy()
    import dayes
    
    
def prevPage():
    pass
Label(
    ws,
    text="This is Third page",
    padx=20,
    pady=20,
    bg='#bfff00'
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Previous Page", 
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)
