from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
import backend as bk
 
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.minsize(1920,1080)
        self.title("versenotes")

def click_start(e):
    widget = e.widget
    widget.startX = e.x
    widget.startY = e.y

def click_hold(e):
    widget = e.widget
    x = widget.winfo_x() - widget.startX + e.x
    y = widget.winfo_y() - widget.startY + e.y
    widget.place(x=x, y=y)

cntrx = 1920/2 
cntry = 900/2
curr_str = ""



root = Root()
#mycanv = Canvas(root, width=1920,height= 900, bg= 'white')
#mycanv.pack(pady=10)

def getverse() -> None:
    # gets verse input
    curr_str = simpledialog.askstring('insert', 'insert a verse to add to the map')
    # adds it to map/pool array
    bk.text_input(curr_str)
    # displays verse in center of map
    mylabl = Label(root, bg='white', anchor= CENTER, text=curr_str)
    mylabl.place(x=cntrx, y=cntry)
    #on left mouse click
    mylabl.bind("<Button-1>", click_start)
    #event on hold lmb and drag
    mylabl.bind("<B1-Motion>", click_hold)




addtxt = ttk.Button(root, text = 'add verse', command = getverse)
addtxt.pack(pady= 5, padx= 50)


root.mainloop()