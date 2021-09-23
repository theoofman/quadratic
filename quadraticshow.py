import math
from tkinter import *
from quadratic import quadratic

def calculate():
    Label(window, text=" "*100).grid(row=4)
    global answer
    aval=a.get()
    bval=b.get()
    cval=c.get()
    if aval and bval and cval:
        answers = quadratic(float(aval),float(bval),float(cval))
        answer = Label(window, text="Answer: "+str(answers[0])+", "+str(answers[1])).grid(row=4)
        text = Label(window, text=answers[2]).grid(row=5)
def exitt():
    exit(code="you suck")
window = Tk()
window.title("Quadratic Calculator")
window.geometry("960x1080")
Label(window, text="What is A?").grid(row=0)
Label(window, text="What is B?").grid(row=1)
Label(window, text="What is C?").grid(row=2)
Button(window, text="Find Answers", command=calculate).grid(row=3)
Button(window, text="Exit", command=exitt).grid(row=6)
a = Entry(window)
b = Entry(window)
c = Entry(window)

a.grid(row=0, column=1)
b.grid(row=1, column=1)
c.grid(row=2, column=1)


window.mainloop()


