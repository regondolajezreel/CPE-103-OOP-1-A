import math
import tkinter as tk

history_list = []

def add():
    res = float(entry1.get()) + float(entry2.get())
    result.set(res)
    update_history("Addition", res)

def subtract():
    res = float(entry1.get()) - float(entry2.get())
    result.set(res)
    update_history("Subtraction", res)

def multiply():
    res = float(entry1.get()) * float(entry2.get())
    result.set(res)
    update_history("Multiplication", res)

def divide():
    try:
        res = float(entry1.get()) / float(entry2.get())
        result.set(res)
        update_history("Division", res)
    except ZeroDivisionError:
        result.set("Error! Division by zero.")

def sqrt():
    res = float(entry3.get()) ** 0.5
    result.set(res)
    update_history("Square Root", res)

def power():
    res = float(entry3.get()) ** float(entry4.get())
    result.set(res)
    update_history("Power", res)

def sin_func():
    try:
        res = math.sin(math.radians(float(entry3.get())))
        result.set(res)
        update_history("Sine", res)
    except ValueError:
        result.set("Invalid Input")

def cos_func():
    try:
        res = math.cos(math.radians(float(entry3.get())))
        result.set(res)
        update_history("Cosine", res)
    except ValueError:
        result.set("Invalid Input")

def tan_func():
    try:
        res = math.tan(math.radians(float(entry3.get())))
        result.set(res)
        update_history("Tangent", res)
    except ValueError:
        result.set("Invalid Input")

def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    result.set("")
    history_list.clear()
    box.delete(0, tk.END)

def update_history(operation, result_value):
    entry = f"{operation}: {result_value}"
    history_list.append(entry)
    box.insert(tk.END, entry)

root = tk.Tk()
root.title("CALCULATOR")
root.geometry("515x350")
root.configure(bg="#ff4900")

result = tk.StringVar()

tk.Label(root, text="Enter 1st number:").place(x=25, y=20)
entry1 = tk.Entry(root)
entry1.place(x=150, y=20)

tk.Label(root, text="Enter 2nd number:").place(x=25, y=60)
entry2 = tk.Entry(root)
entry2.place(x=150, y=60)

tk.Label(root, text="Enter a number:").place(x=150, y=157)
entry3 = tk.Entry(root)
entry3.place(x=250, y=157)

tk.Label(root, text="Power:").place(x=150, y=115)
entry4 = tk.Entry(root)
entry4.place(x=250, y=115)

tk.Button(root, text="Add", command=add).place(x=25, y=105)
tk.Button(root, text="Subtract", command=subtract).place(x=25, y=140)
tk.Button(root, text="Multiply", command=multiply).place(x=25, y=175)
tk.Button(root, text="Divide", command=divide).place(x=25, y=210)

tk.Button(root, text="sqrt()", command=sqrt).place(x=150, y=200)
tk.Button(root, text="pow()", command=power).place(x=200, y=200)
tk.Button(root, text="sin()", command=sin_func).place(x=250, y=200)
tk.Button(root, text="cos()", command=cos_func).place(x=300, y=200)
tk.Button(root, text="tan()", command=tan_func).place(x=350, y=200)

tk.Button(root, text="Clear", command=clear).place(x=405, y=200)


tk.Label(root, text="Result:").place(x=300, y=40)
tk.Entry(root, textvariable=result).place(x=365, y=40)

tk.Label(root, text="History:", font='Arial 10 bold').place(x=25, y=280)
box = tk.Listbox(root, height=5, width=65, bg='#7df176')
box.place(x=100, y=250)

root.mainloop()
