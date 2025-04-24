from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number', bg = "#00a714")
        self.lbl2=Label(win, text='Second number', bg = "#00a714")
        self.lbl3=Label(win, text='Result', bg = "#00a714")
        self.t1=Entry(bd=5)
        self.t2=Entry(bd=5)
        self.t3=Entry(bd=5)
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=75, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=75, y=100)
        self.t2.place(x=200, y=100)
        self.b1 = Button(win, text='Add', bg = "#00a714", command = self.add)
        self.b2 = Button(win, text='Subtract', bg = "#00a714")
        self.b3 = Button(win, text='Multiply', bg="#00a714")
        self.b4 = Button(win, text='Divide', bg="#00a714")
        self.b5 = Button(win, text='Clear', bg="#00a714")
        self.b2.bind('<Button-1>', self.sub)
        self.b3.bind('<Button-1>', self.mult)
        self.b4.bind('<Button-1>', self.div)
        self.b5.bind('<Button-1>', self.clear)
        self.b1.place(x=75, y=200)
        self.b2.place(x=125, y=200)
        self.b3.place(x=200, y=200)
        self.b4.place(x=275, y=200)
        self.b5.place(x=175, y=250)
        self.lbl3.place(x=75, y=150)
        self.t3.place(x=200, y=150)

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def mult(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def div(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 / num2
        self.t3.insert(END, str(result))

    def clear(self, event):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')

window = Tk()
window.configure(bg="#ff4900")
mywin = MyWindow(window)
window.title('CALCULATOR')
window.geometry("400x300+10+10")
window.mainloop()