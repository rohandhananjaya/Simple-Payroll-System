import tkinter as tk
from tkinter import messagebox, ttk

class SimplePayroll:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Payroll v1.0")
        self.root.geometry("600x600")

        self.name_var = tk.StringVar()
        self.rate_var = tk.StringVar()
        self.hours_var = tk.StringVar()
        self.days_var = tk.StringVar()

        self.create_widgets()
        self.create_table()

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

    def create_table(self):
        self.table = ttk.Treeview(self.root)
        self.table['columns'] = ('name', 'gross', 'tax', 'philhealth', 'sss', 'net')
        self.table.column('#0', width=0, stretch=tk.NO)
        self.table.column('name', anchor=tk.CENTER, width=80)
        self.table.column('gross', anchor=tk.CENTER, width=80)
        self.table.column('tax', anchor=tk.CENTER, width=80)
        self.table.column('philhealth', anchor=tk.CENTER, width=80)
        self.table.column('sss', anchor=tk.CENTER, width=80)
        self.table.column('net', anchor=tk.CENTER, width=80)

        self.table.heading('#0', text='', anchor=tk.CENTER)
        self.table.heading('name', text='Name', anchor=tk.CENTER)
        self.table.heading('gross', text='Gross Salary', anchor=tk.CENTER)
        self.table.heading('tax', text='Tax', anchor=tk.CENTER)
        self.table.heading('philhealth', text='Philhealth', anchor=tk.CENTER)
        self.table.heading('sss', text='SSS', anchor=tk.CENTER)
        self.table.heading('net', text='Net Salary', anchor=tk.CENTER)

        self.table.grid(row=5, column=0, columnspan=2)

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

            self.table.insert('', 'end', values=(name, round(gross_salary, 2), round(tax, 2),
                                                 round(philhealth, 2), round(sss, 2), round(net_salary, 2)))

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePayroll(root)
    root.mainloop()