from Tkinter import *

root = Tk()

def callback(event):
    print "clicked at", event.x, event.y 
def callback1(event):
    print "move ",event.x,event.y
frame = Frame(root, width=400, height=400)
frame.bind("<ButtonPress-1>", callback)
##frame.bind("<B1-Motion>",callback1)
frame.pack()

root.mainloop()
