from Tkinter import *

root = Tk()

def callback():
    print "called the callback!"

# create a toolbar
toolbar = Frame(root)

b = Button(toolbar, text="new", width=20, command=callback)
b.pack(side=LEFT, padx=20, pady=20)

b = Button(toolbar, text="open", width=20, command=callback)
b.pack(side=LEFT, padx=20, pady=20)

toolbar.pack(side=TOP, fill=X)

mainloop()