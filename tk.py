from tkinter import  Tk, Label, Button, Entry, Checkbutton


main = Tk ()


#Add Widgets

w =Label(main, text="hi").grid(row = 10)
# w.pack()

button = Button(main, text="Close app", width=30, command=main.destroy)
# button.pack()


Label(main, text="First Name").grid(row=0)
Label(main, text="last Name").grid(row=1)
e1 = Entry(main)
e2 = Entry(main)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

window = Tk()
window.title("com")
window.geometry("40*25")
chk_state = BooleanVar()

# root = Tk()
# root.title("Пример Checkbutton")
# var = Tk()
# checkbutton = Tk.Checkbutton(root, text="Включить функцию", variable=var, onvalue=1, offvalue=0)
# checkbutton.pack()

#Add Widgets

main.mainloop()