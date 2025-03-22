import tkinter as tk
from tkinter import ttk, messagebox


class BirthdateSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Birthdate Selector")
        self.geometry("340x250")
        self.configure(bg="#09bbe7")
        self.iconbitmap("pythonico.ico")
        self.center()

        tk.Label(self, text="Birth Date (DD):", bg="#09bbe7", fg="black").place(x=30, y=30)
        tk.Label(self, text="Birth Month (MM):", bg="#09bbe7", fg="black").place(x=30, y=70)
        tk.Label(self, text="Birth Year (YYYY):", bg="#09bbe7", fg="black").place(x=30, y=110)

        self.dateVar = tk.StringVar()
        self.dateCombo = ttk.Combobox(self, textvariable=self.dateVar, values=[str(i) for i in range(1, 32)])
        self.dateCombo.place(x=180, y=30, width=110)

        self.monthVar = tk.StringVar()
        self.monthCombo = ttk.Combobox(self, textvariable=self.monthVar, values=[str(i) for i in range(1, 13)])
        self.monthCombo.place(x=180, y=70, width=110)

        self.yearVar = tk.StringVar()
        self.yearCombo = ttk.Combobox(self, textvariable=self.yearVar, values=[str(i) for i in range(1980, 2026)])
        self.yearCombo.place(x=180, y=110, width=110)

        tk.Button(self, text="Show Info", command=self.showInfo, bg="#04cf7f", fg="black").place(x=30, y=160, width=80)
        tk.Button(self, text="Clear", command=self.clearSelection, bg="#ff4956", fg="black").place(x=125, y=160, width=80)

    def center(self):
        self.update_idletasks()
        width, height = 340, 250
        x = (self.winfo_screenwidth() - width) // 2
        y = (self.winfo_screenheight() - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

    def showInfo(self):
        messagebox.showinfo("Selected Birthdate",
                            f"You selected (MM/DD/YYYY): {self.monthVar.get()}/{self.dateVar.get()}/{self.yearVar.get()}")

    def clearSelection(self):
        self.dateCombo.set("")
        self.monthCombo.set("")
        self.yearCombo.set("")


if __name__ == "__main__":
    app = BirthdateSelector()
    app.mainloop()