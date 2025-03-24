from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""
 

def clear():
    global expression 
    expression = "" 
    equation.set("") 
    

if __name__ == "__main__":
    
    gui = Tk()
    
    gui.configure(background="light green")
    gui.title("Calc")
    gui.geometry("320x150")
    
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    
    expression_field.grid(columnspan=4,ipadx=70)
    
    button1 = Button(gui, text="1", fg="black", bg="red", height=1, width=7, command=lambda:press(1))
    button1.grid(row=2, column=0)
    
    button2 = Button(gui, text="2", fg="black", bg="red", height=1, width=7, command=lambda:press(2))
    button2.grid(row=2, column=1)
    
    button3 = Button(gui, text="3", fg="black", bg="red", height=1, width=7, command=lambda:press(3))
    button3.grid(row=2, column=2)

    button4 = Button(gui, text="4", fg="black", bg="red", height=1, width=7, command=lambda:press(4))
    button4.grid(row=3, column=0)
    
    button5 = Button(gui, text="5", fg="black", bg="red", height=1, width=7, command=lambda:press(5))
    button5.grid(row=3, column=1)
    
    button6 = Button(gui, text="6", fg="black", bg="red", height=1, width=7, command=lambda:press(6))
    button6.grid(row=3, column=2)

    button7 = Button(gui, text="7", fg="black", bg="red", height=1, width=7, command=lambda:press(7))
    button7.grid(row=4, column=0)
    
    button8 = Button(gui, text="8", fg="black", bg="red", height=1, width=7, command=lambda:press(8))
    button8.grid(row=4, column=1)
    
    button9 = Button(gui, text="9", fg="black", bg="red", height=1, width=7, command=lambda:press(9))
    button9.grid(row=4, column=2)

    button0 = Button(gui, text="0", fg="black", bg="red", height=1, width=7, command=lambda:press(0))
    button0.grid(row=5, column=1)

    tochka = Button(gui, text=".", fg="black", bg="red", height=1, width=7, command=lambda:press("."))
    tochka.grid(row=5, column=0)



   
    plus = Button(gui, text="+", fg="black", bg='red', height= 1, width=7 ,command=lambda:press("+"))
    plus.grid(row=2, column=3)
    equal = Button(gui, text="=", fg="black", bg='red', height= 1, width=7 ,command=equalpress)
    equal.grid(row=5, column=2)
    minus = Button(gui, text="-", fg="black", bg='red', height= 1, width=7 ,command=lambda:press("-"))
    minus.grid(row=4, column=3)
    division = Button(gui, text="/", fg="black", bg='red', height= 1, width=7 ,command=lambda:press("/"))
    division.grid(row=5, column=3)
    mul = Button(gui, text="*", fg="black", bg='red', height= 1, width=7 ,command=lambda:press("*"))
    mul.grid(row=3, column=3)
  
  
    
    
gui.mainloop()