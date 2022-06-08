#import tkinter lib

from tkinter import *


#create the object

window = Tk()


# create a function for click the submit button
def click():
    enter_text = textEntry.get()
    output.delete(0.0,END)
    try:
        define = my_data[enter_text]
    except:
        define='not available'
    output.insert(END,define)

# text box

textbox = Entry(window,width = 50,bg = 'white').grid(row = 0,column = 0,sticky = W)

# label
Label(window, text="Hello pycharm to tkinter",bg='red').grid(row = 0,column=1,sticky=W)



# button
Button(window,text='Submit',bg = 'blue').grid(row = 1,column=1,sticky=W)


# another level
Label(window,text='\nDefination',bg = 'red',fg='white',font = 'aerial 12 bold').grid(row = 1,column=0,sticky=W)

# text box
textEntry = Entry(window,width = 30, bg= 'white')
textEntry.grid(row = 1,column=1,sticky=W)

# text box
output = Text(window,width = 60,height = 10,wrap=WORD,background='white')
output.grid(row = 5,column=0,sticky=W)

# submit button
Button(window,text = 'Submit',width=10,command=click,bg ='red',fg='black').grid(row=3,column=0,sticky=W)


# enter something to know----> create a lable for this!!

# create a data for the project.
# make a dict

my_data = {
    'animal':['dog','cat'],
    'bug':'Data not available'
}







window.mainloop()


