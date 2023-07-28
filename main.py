import tkinter as tk
from tkinter import messagebox

class SimplePayroll:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Payroll v1.0")
        self.root.geometry("400x400")

        self.name_var = tk.StringVar()
        self.rate_var = tk.StringVar()
        self.hours_var = tk.StringVar()
        self.days_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text='Name:').grid(row=0)
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(self.root, text='Rate per hour:').grid(row=1)
        tk.Entry(self.root, textvariable=self.rate_var).grid(row=1, column=1)

        tk.Label(self.root, text='Hours per day:').grid(row=2)
        tk.Entry(self.root, textvariable=self.hours_var).grid(row=2, column=1)

        tk.Label(self.root, text='Days worked:').grid(row=3)
        tk.Entry(self.root, textvariable=self.days_var).grid(row=3, column=1)

        tk.Button(self.root, text='Calculate Payroll').grid(row=4, column=1)



if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePayroll(root)
    root.mainloop()
