from tkinter import *

#Define main window
window = Tk()
window.title("Calculator")
window.geometry("398x238")
window.resizable(False, False)
#Define functions
operator = ""


def click_button(numbers):
    global operator
    operator = operator + str(numbers)
    text.delete(0, END)
    text.insert(END, operator)

def answer():
    global operator
    result = str(eval(operator))
    text.delete(0,END)
    text.insert(0,result)
    operator = ""

def clear():
    global operator
    operator = ""
    text.delete(0,END)

#Define frame
frame = Frame(window, width=398, height=238)
frame.pack()

#Define field
text = Entry(frame, font=("calibre", 16), bd=4, width=32)
text.grid(row=0, column=0, columnspan=4)

#Define Buttons
btn7 = Button(frame, text=7, font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
              command=lambda: click_button(7))
btn7.grid(row=1, column=0, columnspan=1)

btn8 = Button(frame, text=8, font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
              command=lambda: click_button(8))
btn8.grid(row=1, column=1, columnspan=1)

btn9 = Button(frame, text=9, font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
              command=lambda: click_button(9))
btn9.grid(row=1, column=2, columnspan=1)

btnAdd = Button(frame, text="+", font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
                command=lambda: click_button("+"))
btnAdd.grid(row=1, column=3, columnspan=1)

btn4 = Button(frame, text=4, font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
              command=lambda: click_button(4))
btn4.grid(row=2, column=0, columnspan=1)

btn5 = Button(frame, text=5, font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
              command=lambda: click_button(5))
btn5.grid(row=2, column=1, columnspan=1)

btn6 = Button(frame, text=6, font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
              command=lambda: click_button(6))
btn6.grid(row=2, column=2, columnspan=1)

btnMinus = Button(frame, text="-", font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
                  command=lambda: click_button("-"))
btnMinus.grid(row=2, column=3, columnspan=1)

btn1 = Button(frame, text=1, font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
              command=lambda: click_button(1))
btn1.grid(row=3, column=0, columnspan=1)

btn2 = Button(frame, text=2, font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
              command=lambda: click_button(2))
btn2.grid(row=3, column=1, columnspan=1)

btn3 = Button(frame, text=3, font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
              command=lambda: click_button(3))
btn3.grid(row=3, column=2, columnspan=1)

btnMulti = Button(frame, text="*", font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
                  command=lambda: click_button("*"))
btnMulti.grid(row=3, column=3, columnspan=1)

btnAns = Button(frame, text="Ans", font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,command=answer)
btnAns.grid(row=4, column=0, columnspan=1)

btnClr = Button(frame, text="Clear", font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,command=clear)
btnClr.grid(row=4, column=1, columnspan=1)

btn0 = Button(frame, text=0, font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
              command=lambda: click_button(0))
btn0.grid(row=4, column=2, columnspan=1)

btnDiv = Button(frame, text="/", font=("calibre", 16, "bold"), fg="Yellow", bg="Red4", width=6, bd=6,
                command=lambda: click_button("/"))
btnDiv.grid(row=4, column=3, columnspan=1)
window.mainloop()
