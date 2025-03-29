from tkinter import *

window = Tk()
window.title("Using Grid Manager")
window.geometry("400x200")

txtfld1 = Entry(window, justify="center")
txtfld1.grid(row=0, column=0)
txtfld1.insert(END, "row 0, column 0")

txtfld2 = Entry(window, justify="center")
txtfld2.grid(row=0, column=1)
txtfld2.insert(END, "row 0, column 1")

txtfld3 = Entry(window, justify="center")
txtfld3.grid(row=0, column=2)
txtfld3.insert(END, "row 0, column 2")

txtfld4 = Entry(window, justify="center")
txtfld4.grid(row=1, column=0)
txtfld4.insert(END, "row 1, column 0")

txtfld4 = Entry(window, justify="center")
txtfld4.grid(row=1, column=1)
txtfld4.insert(END, "row 1, column 1")

txtfld5 = Entry(window, justify="center")
txtfld5.grid(row=1, column=2)
txtfld5.insert(END, "row 1, column 2")

listbox = Listbox(window)
listbox.grid(row=2, column=1)

yscroll = Scrollbar(window)
yscroll.grid(row=2,column=2, sticky="nsw")
listbox.config(yscrollcommand=yscroll.set)

for x in range(51):
    listbox.insert(0, x)
    yscroll.config(command=listbox.yview())



window.mainloop()