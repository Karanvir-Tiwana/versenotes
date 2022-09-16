from asyncio.windows_events import NULL
from cProfile import label
from cmath import e
from mimetypes import common_types
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
import backend as bk
 
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.maxsize(1920,1080)
        self.minsize(1920//4,1080//4)
        self.title("versenotes")

cntrx = 1920/2 
cntry = 900/2
curr_str = ""
highlighted_list = []

def click_start(e):
    widget = e.widget
    widget.startX = e.x
    widget.startY = e.y

def click_hold(e):
    widget = e.widget
    x = widget.winfo_x() - widget.startX + e.x
    y = widget.winfo_y() - widget.startY + e.y
    widget.place(x=x, y=y)

def delete_selected(e):
    widget = e.widget
    widget.destroy()

def highlight_selected(e):
    widget = e.widget
    if widget in highlighted_list:
        widget.configure(background="white")
        highlighted_list.remove(widget)
    else:
        highlighted_list.append(widget)
        widget.configure(background="blue")


def done_highlight():
    for w in highlighted_list:
        w.configure(background="red")
    highlighted_list.clear()



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
    #event on middle mouse click
    mylabl.bind("<Button-2>", delete_selected)
    #event on hold lmb and drag
    mylabl.bind("<B1-Motion>", click_hold)
    mylabl.bind("<Button-3>", highlight_selected)    

addtxt = ttk.Button(root, text = 'add verse', command = getverse)
addtxt.pack(pady= 5, padx= 50)
# allows to link selected verses
link_label = ttk.Button(root, text="link selected", command = done_highlight)
link_label.pack(pady=20, padx=100)


root.mainloop()