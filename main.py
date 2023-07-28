import tkinter as tk
from tkinter import messagebox, ttk

class SimplePayroll:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Payroll v1.0")
        self.root.geometry("780x400")

        self.name_var = tk.StringVar()
        self.rate_var = tk.StringVar()
        self.hours_var = tk.StringVar()
        self.days_var = tk.StringVar()

        self.create_widgets()
        self.create_table()

    def create_widgets(self):
        tk.Label(self.root, text='Name of the employee:').grid(sticky = 'n',row=0)
        tk.Entry(self.root, textvariable=self.name_var).grid(sticky = 'w' , row=0, column=1)
        tk.Label(self.root, text='Rate per hour (Rs.):').grid(sticky = 'n',row=1)
        tk.Entry(self.root, textvariable=self.rate_var).grid(sticky = 'w' ,row=1, column=1)
        tk.Label(self.root, text='Hours per day:').grid(sticky = 'n',row=2)
        tk.Entry(self.root, textvariable=self.hours_var).grid(sticky = 'w' ,row=2, column=1)
        tk.Label(self.root, text='Days worked:').grid(sticky = 'n',row=3)
        tk.Entry(self.root, textvariable=self.days_var).grid(sticky = 'w' ,row=3, column=1)
        tk.Button(self.root, text='Calculate Payroll', command=self.calculate_payroll).grid(sticky = 'w' ,row=4, column=1)

    def create_table(self):
        self.table = ttk.Treeview(self.root)
        self.table['columns'] = ('name', 'gross', 'tax', 'healthinsure', 'rs', 'net')
        self.table.column('#0', width=0, stretch=tk.NO)
        self.table.column('name', anchor=tk.CENTER, width=80)
        self.table.column('gross', anchor=tk.CENTER, width=150)
        self.table.column('tax', anchor=tk.CENTER, width=80)
        self.table.column('healthinsure', anchor=tk.CENTER, width=150)
        self.table.column('rs', anchor=tk.CENTER, width=150)
        self.table.column('net', anchor=tk.CENTER, width=120)

        self.table.heading('#0', text='', anchor=tk.CENTER)
        self.table.heading('name', text='Name', anchor=tk.CENTER)
        self.table.heading('gross', text='Gross Salary (Rs.)', anchor=tk.CENTER)
        self.table.heading('tax', text='Tax (Rs.)', anchor=tk.CENTER)
        self.table.heading('healthinsure', text='Health Insurance (Rs.)', anchor=tk.CENTER)
        self.table.heading('rs', text='Retirement Savings (Rs.)', anchor=tk.CENTER)
        self.table.heading('net', text='Net Salary (Rs.)', anchor=tk.CENTER)

        self.table.grid(row=5, column=0, columnspan=2)

    def calculate_payroll(self):
        try:
            name = self.name_var.get()
            rate = float(self.rate_var.get())
            hours = float(self.hours_var.get())
            days = float(self.days_var.get())

            gross_salary = rate * hours * days
            tax = gross_salary * 0.15
            healthinsure = gross_salary * 0.05
            ret_sv = gross_salary * 0.02

            net_salary = gross_salary - tax - healthinsure - ret_sv

            messagebox.showinfo("Simple Payroll v1.0", 
                                            f"Employee Name: {name}\n"
                                            f"Gross Salary: Rs.{gross_salary}\n"
                                            f"Deductions:\n"
                                            f"Tax: Rs.{tax}\n"
                                            f"Health insurance: {healthinsure}\n"
                                            f"Retirement Savings : Rs. {ret_sv}\n"
                                            f"Net Salary: Rs. {net_salary}")

            self.table.insert('', 'end', values=(name, round(gross_salary, 2), round(tax, 2),
                                                 round(healthinsure, 2), round(ret_sv, 2), round(net_salary, 2)))

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePayroll(root)
    root.mainloop()