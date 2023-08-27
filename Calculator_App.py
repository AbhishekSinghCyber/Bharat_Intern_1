from tkinter import *

# Define main Window
cyber = Tk()
cyber.title("Simple Calculator")
cyber.geometry("698x538")
cyber.resizable()
cyber.iconbitmap("calculator.ico")
cyber.maxsize()
cyber.config(background="spring green")
# Define Functions
operator = ""


def click_buttons(numbers):
    global operator
    operator = operator + str(numbers)
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)


def clear():
    global operator
    operator = ""
    calculatorField.delete(0, END)


def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0, END)
    calculatorField.insert(0, result)
    operator = ""


# define frame and field
calculatorFrame = Frame(cyber, width=698, height=538)
calculatorFrame.pack()

calculatorField = Entry(calculatorFrame, font=("Arial", 16, "bold"), bd=20, width=30)
calculatorField.grid(row=0, column=0, columnspan=4)

# Define Button
button7 = Button(calculatorFrame, text=7, font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6, bd=6,
                 command=lambda: click_buttons(7))
button7.grid(row=1, column=0, columnspan=1)
button8 = Button(calculatorFrame, text=8, font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6, bd=6,
                 command=lambda: click_buttons(8))
button8.grid(row=1, column=1, columnspan=1)
button9 = Button(calculatorFrame, text=9, font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6, bd=6,
                 command=lambda: click_buttons(9))
button9.grid(row=1, column=2, columnspan=1)
buttonPlus = Button(calculatorFrame, text="+", font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6,
                    bd=6, command=lambda: click_buttons("+"))
buttonPlus.grid(row=1, column=3, columnspan=1)

button4 = Button(calculatorFrame, text=4, font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6, bd=6,
                 command=lambda: click_buttons(4))
button4.grid(row=2, column=0, columnspan=1)
button5 = Button(calculatorFrame, text=5, font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6, bd=6,
                 command=lambda: click_buttons(5))
button5.grid(row=2, column=1, columnspan=1)
button6 = Button(calculatorFrame, text=6, font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6, bd=6,
                 command=lambda: click_buttons(6))
button6.grid(row=2, column=2, columnspan=1)
buttonMinus = Button(calculatorFrame, text="-", font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6,
                     bd=6, command=lambda: click_buttons("-"))
buttonMinus.grid(row=2, column=3, columnspan=1)
button1 = Button(calculatorFrame, text=1, font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6, bd=6,
                 command=lambda: click_buttons(1))
button1.grid(row=3, column=0, columnspan=1)
button2 = Button(calculatorFrame, text=2, font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6, bd=6,
                 command=lambda: click_buttons(2))
button2.grid(row=3, column=1, columnspan=1)
button3 = Button(calculatorFrame, text=3, font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6, bd=6,
                 command=lambda: click_buttons(3))
button3.grid(row=3, column=2, columnspan=1)
buttonMulti = Button(calculatorFrame, text="*", font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6,
                     bd=6, command=lambda: click_buttons("*"))
buttonMulti.grid(row=3, column=3, columnspan=1)
buttonAns = Button(calculatorFrame, text="Ans", font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6,
                   bd=6, command=answer)
buttonAns.grid(row=4, column=0, columnspan=1)
buttonClear = Button(calculatorFrame, text="Clear", font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6,
                     bd=6, command=clear)
buttonClear.grid(row=4, column=1, columnspan=1)
buttonZero = Button(calculatorFrame, text="0", font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6,
                    bd=6, command=lambda: click_buttons(0))
buttonZero.grid(row=4, column=2, columnspan=1)
buttonDiv = Button(calculatorFrame, text="/", font=("Arial", 16, "bold"), fg="ivory", bg="deep sky blue", width=6, bd=6,
                   command=lambda: click_buttons("/"))
buttonDiv.grid(row=4, column=3, columnspan=1)
cyber.mainloop()
