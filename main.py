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

        tk.Button(self.root, text='Calculate Payroll', command=self.calculate_payroll).grid(row=4, column=1)

    def calculate_payroll(self):
        try:
            name = self.name_var.get()
            rate = float(self.rate_var.get())
            hours = float(self.hours_var.get())
            days = float(self.days_var.get())

            gross_salary = rate * hours * days
            tax = gross_salary * 0.15
            philhealth = gross_salary * 0.05
            sss = gross_salary * 0.02

            net_salary = gross_salary - tax - philhealth - sss

            messagebox.showinfo("Payroll", f"Gross Salary: {gross_salary}\n"
                                           f"Deductions:\n"
                                           f"Tax: {tax}\n"
                                           f"Philhealth: {philhealth}\n"
                                           f"SSS: {sss}\n"
                                           f"Net Salary: {net_salary}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePayroll(root)
    root.mainloop()
