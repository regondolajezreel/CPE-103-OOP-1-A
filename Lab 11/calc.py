import tkinter as tk
import math
import re

def press(value):
    current = displayVar.get()
    displayVar.set(current + str(value))
    tryInstantEval()

def backspace():
    current = displayVar.get()
    displayVar.set(current[:-1])

def tryInstantEval():
    expr = displayVar.get()
    match = re.fullmatch(r"(sin|cos|tan)\((\-?\d+(\.\d*)?)\)", expr)
    if match:
        func, val, _ = match.groups()
        val = float(val)
        radians = math.radians(val)
        result = getattr(math, func)(radians)
        displayVar.set(str(result))

def equalPress():
    try:
        expr = displayVar.get()
        expr = expr.replace("sin(", "math.sin(math.radians(")
        expr = expr.replace("cos(", "math.cos(math.radians(")
        expr = expr.replace("tan(", "math.tan(math.radians(")
        expr = expr.replace("exp(", "**(")
        result = str(eval(expr, {"__builtins__": None, "math": math}, math.__dict__))
        displayVar.set(result)
    except Exception as e:
        displayVar.set("Error")

def clear():
    displayVar.set("")

def onKey(event):
    key = event.char
    if event.keysym == "Return":
        equalPress()
        return "break"
    elif event.keysym == "BackSpace":
        backspace()
        return "break"
    elif key.lower() == "c":
        clear()
        return "break"



calcu = tk.Tk()
calcu.title("Calculator")
calcu.geometry("360x590")
calcu.configure(bg="#CFE2F3")

displayFrame = tk.Frame(calcu, bg="#bfe1ff", bd=10, relief="ridge")
displayFrame.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="we")

displayVar = tk.StringVar()
displayEntry = tk.Entry(
    displayFrame,
    textvariable=displayVar,
    font=("Arial", 20),
    bg="#c9e1f7",
    justify="right"
)
displayEntry.pack(fill="x", ipadx=8, ipady=8)

buttons = [
    ["exp","⌫", "C"],
    ["sin", "cos", "tan", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "(", ")"],
    ["="]
]

# --- Button frame ---
buttonFrame = tk.Frame(calcu, bg="#CFE2F3")
buttonFrame.grid(row=1, column=0, columnspan=4, sticky="nsew")

for i in range(4):
    buttonFrame.columnconfigure(i, weight=1)

# --- Create buttons ---
for r, row in enumerate(buttons):
    for c, btnText in enumerate(row):
        if btnText == "exp":
            btn = tk.Button(buttonFrame, text="exp", font=("Arial", 16, "bold"), height=2, bg="#a7d6ff", command=lambda: press("exp("))
            btn.grid(row=r, column=0, padx=2, pady=2, sticky="we")
        elif btnText == "C":
            btn = tk.Button(buttonFrame, text="C", font=("Arial", 16, "bold"), height=2, bg="#ffaaaa", command=clear)
            btn.grid(row=r, column=2, columnspan=2, sticky="we", padx=2, pady=2)
        elif btnText == "⌫":
            btn = tk.Button(buttonFrame, text="⌫", font=("Arial", 16, "bold"), height=2, bg="#ffccaa", command=backspace)
            btn.grid(row=r, column=1, sticky="we", padx=2, pady=2)
        elif btnText == "=":
            btn = tk.Button(buttonFrame, text="=", font=("Arial", 16, "bold"), height=2, bg="#a7d6ff", command=equalPress)
            btn.grid(row=r, column=0, columnspan=4, sticky="we", padx=2, pady=2)
        else:
            if btnText in ["sin", "cos", "tan"]:
                displayValue = f"{btnText}("
            else:
                displayValue = btnText
            btn = tk.Button(
                buttonFrame,
                text=btnText,
                font=("Arial", 16, "bold"),
                height=2,
                bg="#a7d6ff",
                command=lambda b=displayValue: press(b)
            )
            btn.grid(row=r, column=c, padx=2, pady=2, sticky="we")

displayEntry.bind("<KeyPress>", onKey)

calcu.mainloop()
