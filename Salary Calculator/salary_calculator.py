import tkinter as tk
from tkinter import ttk, messagebox

#Main window configuration
root = tk.Tk()
root.title("Salary Calculator")

result = tk.StringVar()

style = ttk.Style()
style.theme_use('xpnative')

#Interface layout
ttk.Label(root, text="Hours Worked:").grid(row=0, column=0, padx=10, pady=5)
hours_entry = ttk.Entry(root)
hours_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Hourly Rate:").grid(row=1, column=0, padx=10, pady=5)
hourly_rate_entry = ttk.Entry(root)
hourly_rate_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Overtime Hours:").grid(row=2, column=0, padx=10, pady=5)
overtime_hours_entry = ttk.Entry(root)
overtime_hours_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Overtime Rate:").grid(row=3, column=0, padx=10, pady=5)
overtime_rate_entry = ttk.Entry(root)
overtime_rate_entry.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(root, text="Deductions:").grid(row=4, column=0, padx=10, pady=5)
deductions_entry = ttk.Entry(root)
deductions_entry.grid(row=4, column=1, padx=10, pady=5)

def calculate_salary():
    try:
        hours = float(hours_entry.get())
        hourly_rate = float(hourly_rate_entry.get())
        overtime_hours = float(overtime_hours_entry.get()) if overtime_hours_entry.get() else 0
        overtime_rate = float(overtime_rate_entry.get()) if overtime_rate_entry.get() else 0
        deductions = float(deductions_entry.get()) if deductions_entry.get() else 0

        base_salary = hours * hourly_rate
        overtime_salary = overtime_hours * overtime_rate
        gross_salary = base_salary + overtime_salary
        net_salary = gross_salary - deductions

        result.set(f"The net salary is: ${net_salary:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

ttk.Button(root, text="Calculate", command=calculate_salary).grid(row=5, column=0, columnspan=2, pady=10)

ttk.Label(root, textvariable=result).grid(row=6, column=0, columnspan=2, pady=10)

#Starting the interface loop
root.mainloop()
