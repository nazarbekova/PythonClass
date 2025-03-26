from tkinter import Tk, Label, Button, Entry, Checkbutton, BooleanVar, Radiobutton, IntVar, Listbox, Scrollbar

main = Tk()

# Add Widgets
w = Label(main, text="hi").grid(row=10)

button = Button(main, text="Close app", width=30, command=main.destroy)


Label(main, text="First Name").grid(row=0)
Label(main, text="Last Name").grid(row=1)

e1 = Entry(main)
e2 = Entry(main)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

window = main  
window.title("com")

window.geometry("400x250") 
chk_state = BooleanVar()

root = Tk()  
root.title("Пример Checkbutton")

var = BooleanVar()
checkbutton = Checkbutton(root, text="Включить функцию", variable=var, onvalue=1, offvalue=0)
checkbutton.pack()


radio_var = IntVar()
r1 = Radiobutton(root, text="male", variable=radio_var, value=1)
r2 = Radiobutton(root, text="female", variable=radio_var, value=2)
r1.pack()
r2.pack()

listbox = Listbox(root, height=4)
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.insert(4, "Any other")

listbox.pack()
scrollbar.config(command=listbox.yview)

text_listbox = Listbox(root, height=6, width=30)
scrollbar_text = Scrollbar(root)
scrollbar_text.pack(side="right", fill="y")

for i in range(26, 36):
    text_listbox.insert("end", f"This is line number {i}")

text_listbox.pack()
scrollbar_text.config(command=text_listbox.yview)

# Add Widgets
main.mainloop()