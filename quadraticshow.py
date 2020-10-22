import math
from tkinter import *
from quadratic import quadratic

def calculate():
    aval=a.get()
    bval=b.get()
    cval=c.get()
    if aval and bval and cval:
        answers = quadratic(float(aval),float(bval),float(cval))
        answer = Label(window, text="Answer: "+str(answers)).grid(row=4)
window = Tk()
Label(window, text="What is A?").grid(row=0)
Label(window, text="What is B?").grid(row=1)
Label(window, text="What is C?").grid(row=2)
Button(window, text="Find Answers", command=calculate).grid(row=3)
a = Entry(window)
b = Entry(window)
c = Entry(window)

a.grid(row=0, column=1)
b.grid(row=1, column=1)
c.grid(row=2, column=1)


window.mainloop()


