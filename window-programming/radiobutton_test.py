from tkinter import *

window = Tk()

def myFunc():
    if var.get() == 1:
        label.configure(text="옵션 1")
    elif var.get() == 2:
        label.configure(text="옵션 2")
    else :
        label.configure(text="옵션 3")
        
var = IntVar()
rbList = [None] * 3
label = Label(window, text ="선택한 옵션: ", fg ="red")

for i in range(0, len(rbList)):
    rbList[i] = Radiobutton(window, text = "옵션 "+str(i), variable = var, value = i+1, command = myFunc)
    rbList[i].pack()

label.pack()

window.mainloop()
