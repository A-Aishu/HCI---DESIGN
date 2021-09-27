from tkinter import *
  

root =  Tk ()
  

root.geometry( "1000x1000" )
  

def show():
    label.config( text = clicked.get() )
  
options = [
    " i phone XR",
    " i phone SE",
    " i phone 11",
    " i phone 11 PRO ",
    " i phone 12",
    " i phone 12 PRO",
    " i phone 12 Max "
]
  

clicked = StringVar()
  

clicked.set( "APPLE " )
  

drop = OptionMenu( root , clicked , *options )
drop.pack()
  

button = Button( root , text = "click Me" , command = show ).pack()
  
label = Label( root , text = " " )
label.pack()
  

root.mainloop()
