import tkinter as tk
from tkinter import messagebox
from library.classes_project_9 import Budget

def main():
    m = tk.Tk()
    m.title("Budget Buddy")
    m.geometry("400x400")
    m.configure(bg="#f0f8ff")

    # --- Title ---
    tk.Label(
        m,
        text="💰 Budget Buddy 💰",
        font=("Arial", 16, "bold"),
        bg="#f0f8ff"
    ).pack(pady=10)

    # --- User Inputs ---
    tk.Label(m, text="Enter your Name", bg="#f0f8ff").pack()
    nameEntry = tk.Entry(m)
    nameEntry.pack(pady=5)

    tk.Label(m, text="Enter your income ($)", bg="#f0f8ff").pack()
    incomeEntry = tk.Entry(m)
    incomeEntry.pack(pady=5)

    tk.Label(m, text="Enter your grocery expenses ($)", bg="#f0f8ff").pack()
    groceryExpensesEntry = tk.Entry(m)
    groceryExpensesEntry.pack(pady=5)

    tk.Label(m, text="Enter your car expenses ($)", bg="#f0f8ff").pack()
    carExpensesEntry = tk.Entry(m)
    carExpensesEntry.pack(pady=5)

    # --- Function to show summary ---
    def open_summary_window():
        try:
            income = float(incomeEntry.get())
            grocery_amount = float(groceryExpensesEntry.get())
            car_amount = float(carExpensesEntry.get())
            name = nameEntry.get().strip()

            if not name:
                messagebox.showerror("Error", "Please enter your name.")
                return

            groceries = Budget("Groceries")
            car = Budget("Car")

            groceries.expenses.append(("All", grocery_amount))
            car.expenses.append(("All", car_amount))

            grocery_total = groceries.get_expenses()
            car_total = car.get_expenses()
            total_expenses = grocery_total + car_total
            balance = income - total_expenses

            # --- Create Summary Text ---
            summary = f"""
Name: {name}
Income: ${income:.2f}
Groceries Total: ${grocery_total:.2f}
Car Total: ${car_total:.2f}
Total Expenses: ${total_expenses:.2f}
Remaining Balance: ${balance:.2f}
"""

            # --- Show Summary in New Window ---
            new_window = tk.Toplevel(m)
            new_window.title("Budget Summary")
            tk.Label(new_window, text=summary, justify="left", font=("Courier", 10)).pack(padx=10, pady=10)

            # --- Save Summary to File ---
            with open("Budget Buddy Report.txt", "w") as file:
                file.write(summary)

            messagebox.showinfo("Report Saved", "Summary saved to 'Budget Buddy Report.txt'!")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for income and expenses.")

    # --- Button ---
    tk.Button(m, text="Generate Summary", bg="#87ceeb", command=open_summary_window).pack(pady=15)

    m.mainloop()

if __name__ == "__main__":
    main()
