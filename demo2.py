from tkinter import *

window = Tk()
window.title("Using Grid Manager")
window.geometry("400x200")

listbox = Listbox(window)
listbox.pack(side=LEFT, fill=BOTH, expand=True)

yscroll = Scrollbar(window)
yscroll.pack(side=RIGHT, fill=BOTH)

for x in range(51):
    listbox.insert(0, x)
    yscroll.config(command=listbox.yview())

listbox.config(yscrollcommand=yscroll.set)
yscroll.config(command=listbox.yview)



window.mainloop()