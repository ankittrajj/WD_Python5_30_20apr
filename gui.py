#import tkinter lib

from tkinter import *


#create the object

window = Tk()

# text box

textbox = Entry(window,width = 50,bg = 'white').grid(row = 0,column = 0,sticky = W)

# label
Label(window, text="Hello pycharm to tkinter",bg='red').grid(row = 0,column=1,sticky=W)



# button
Button(window,text='Submit',bg = 'blue').grid(row = 1,column=1,sticky=W)











window.mainloop()


