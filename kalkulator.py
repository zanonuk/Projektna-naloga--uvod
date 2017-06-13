from tkinter import *
#import parser
from math import *
pm = __import__("model")
okno = Tk()
okno.title("Kalkulator")
i = 0

def vnesist(stevilo):
    global i
    display.insert(i,stevilo)
    i+=1
def vnesi(stevilo):
    global i
    i+=1
    return stevilo
def vnesioperator(operator):
    global i
    lenght=len(operator)
    display.insert(i,operator)
    i+=lenght

def pocisti():
    display.delete(0,END)

def pripravi():
    izraz=display.get()
    pocisti()
    izraz=pm.izracunaj(izraz)
    display.insert(0,eval (izraz))

gumbi = Frame(okno)
display = Entry(okno, font = ("Calibri", 13))
display.grid(row = 1, columnspan = 4    , sticky = W+E)

    
gumb1 = Button(okno, text = "1",height = 1, width = 3, command = lambda : display.insert(i,vnesi(1)))
gumb1.grid(row=4, column=1)
gumb2 = Button(okno, text = "2",height = 1, width = 3, command = lambda : vnesist(2))
gumb2.grid(row=5, column=1)
gumb3 = Button(okno, text = "3", height = 1, width = 3, command = lambda : vnesist(3))
gumb3.grid(row=6, column=1)
gumb4 = Button(okno, text = "4",height = 1, width = 3, command = lambda : vnesist(4))
gumb4.grid(row=4, column = 2)
gumb5 = Button(okno, text = "5",height = 1, width = 3, command = lambda : vnesist(5))
gumb5.grid(row=5, column=2)
gumb6 = Button(okno, text = "6",height = 1, width = 3, command = lambda : vnesist(6))
gumb6.grid(row=6, column=2)
gumb7 = Button(okno, text = "7",height = 1, width = 3, command = lambda : vnesist(7))
gumb7.grid(row=4, column=3)
gumb8 = Button(okno, text = "8", height = 1, width = 3, command = lambda : vnesist(8))
gumb8.grid(row=5, column=3)
gumb9 = Button(okno, text = "9",height = 1, width = 3, command = lambda : vnesist(9))
gumb9.grid(row=6, column=3)
gumb0 = Button(okno, text = "0", height = 1, width = 3, command = lambda : vnesist(0))
gumb0.grid(row=7, column=1)
gumb10 = Button(okno, text = "=", height = 1, width = 12, command = pripravi)
gumb10.grid(row=7, column=2, columnspan = 2)
gumb11 = Button(okno, text = "+", height = 1, width = 3, command = lambda : vnesioperator("+"))
gumb11.grid(row=4, column=4)
gumb12 = Button(okno, text = "-", height = 1, width = 3, command = lambda : vnesioperator("-"))
gumb12.grid(row=5, column=4)
gumb13 = Button(okno, text = ":", height = 1, width = 3, command = lambda : vnesioperator(":"))
gumb13.grid(row=6, column=4)
gumb17 = Button(okno, text = "*", height = 1, width = 3, command = lambda : vnesioperator("*"))
gumb17.grid(row=7, column=4)
gumb14 = Button(okno, text = "sin",height = 1, width = 3, command = lambda : vnesioperator("sin"))
gumb14.grid(row=4, column=5)
gumb15 = Button(okno, text = "cos",height = 1, width = 3, command = lambda : vnesioperator("cos"))
gumb15.grid(row=5, column=5)
gumb16 = Button(okno, text = "tan", height = 1, width = 3, command = lambda : vnesioperator("tan"))
gumb16.grid(row=6, column=5)
gumb18 = Button(okno, text = "C", height = 1, width = 3, command=pocisti)
gumb18.grid(row=7, column=5)

okno.mainloop()
