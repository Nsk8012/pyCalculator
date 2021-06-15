from tkinter import *

#Install Application
window = Tk()
window.title("Calculator")

#Adding icon to the application
window.call('wm', 'iconphoto', window._w, PhotoImage(file="/Users/Nsk/Desktop/Project/Calculator/calculator.png"))

#Enter tab
entry = Entry(window, width=15, bd=5)
entry.grid(row=0,column=0,columnspan=2)

#Click Buttton Funtion to return values
def buttonClick(num):
    cn = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(cn)+str(num))

#Addition Function
def buttonAdd():
    n = entry.get()
    global firstNum
    global math
    math = "ADD"
    firstNum = float(n)
    entry.delete(0, END)

#Subtraction Function
def buttonSub():
    n = entry.get()
    global firstNum
    global math
    math  = "SUB"
    firstNum = float(n)
    entry.delete(0, END)

#Multiplication function
def buttonMul():
    n = entry.get()
    global firstNum
    global math
    math  = "MUL"
    firstNum = float(n)
    entry.delete(0, END)

#Division function
def buttonDiv():
    n = entry.get()
    global firstNum
    global math
    math  = "DIV"
    firstNum = float(n)
    entry.delete(0, END)

#Equalising function
def buttonEq():
    secNum = entry.get()
    secNum = float(secNum)
    entry.delete(0, END)
    if math == "ADD":
        finalNum = firstNum + secNum
    elif math == "SUB":
        finalNum = firstNum - secNum
    elif math == "MUL":
        finalNum = firstNum * secNum
    elif math == "DIV":
        finalNum = firstNum / secNum
    #Display if only decimal is required
    if finalNum % 1 == 0:
        entry.insert(0, int(finalNum))
    else:
        entry.insert(0, float(finalNum))        

#To clear everything function
def buttonClear():
    entry.delete(0, END)

#Adding Number buttons
button9 = Button(window, text="9", padx="30", pady="30", command=  lambda: buttonClick(9))
button8 = Button(window, text="8", padx="30", pady="30", command= lambda: buttonClick(8))
button7 = Button(window, text="7", padx="30", pady="30", command= lambda: buttonClick(7))
button6 = Button(window, text="6", padx="30", pady="30", command= lambda: buttonClick(6))
button5 = Button(window, text="5", padx="30", pady="30", command= lambda: buttonClick(5))
button4 = Button(window, text="4", padx="30", pady="30", command= lambda: buttonClick(4))
button3 = Button(window, text="3", padx="30", pady="30", command= lambda: buttonClick(3))
button2 = Button(window, text="2", padx="30", pady="30", command= lambda: buttonClick(2))
button1 = Button(window, text="1", padx="30", pady="30", command= lambda: buttonClick(1))
button0 = Button(window, text="0", padx="30", pady="30", command= lambda: buttonClick(0))

#Adding functional buttons
buSub= Button(window,text="-", padx="31", pady="30", command= buttonSub)
buMul= Button(window,text="*", padx="31", pady="30", command= buttonMul)
buDiv= Button(window,text="/", padx="31.5", pady="30", command= buttonDiv)
buClr= Button(window,text="C", padx="25", pady="10", command= buttonClear)
buAdd= Button(window,text="+", padx="30", pady="30", command= buttonAdd)
buEql= Button(window,text="=", padx="29.5", pady="30", command= buttonEq)

#Positioning those buttons
button9.grid(row=1, column=2, columnspan=1)
button8.grid(row=1, column=1, columnspan=1)
button7.grid(row=1, column=0, columnspan=1)
button6.grid(row=2, column=2, columnspan=1)
button5.grid(row=2, column=1, columnspan=1)
button4.grid(row=2, column=0, columnspan=1)
button3.grid(row=3, column=2, columnspan=1)
button2.grid(row=3, column=1, columnspan=1)
button1.grid(row=3, column=0, columnspan=1)

button0.grid(row=4, column=1, columnspan=1)
buSub.grid(row=4,column=0, columnspan=1)
buDiv.grid(row=4,column=2, columnspan=1)
buAdd.grid(row=5,column=0, columnspan=1)
buMul.grid(row=5,column=1, columnspan=1)
buEql.grid(row=5,column=2, columnspan=1)

buClr.grid(row=0,column=2, columnspan=1)

#To Close the application
window.mainloop()