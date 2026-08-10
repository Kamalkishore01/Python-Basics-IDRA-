import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Creating Csv file 
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])

# Adding a new expense*****************
def add_expense():
    print("\n===== Add Expense =====")
    # Get and validate date
    date = input("Enter date (DD-MM-YYYY): ")

    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format! Please use DD-MM-YYYY.")
        return

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

#Get and validate amount
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    note = input("Enter note (optional): ").strip()

# Save expense to CSV
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("Expense added successfully. ")
# View all expenses
def view_expenses():
    print("\n========== All Expenses ==========")

    total_amount = 0
    expense_found = False

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for expense in reader:
                expense_found = True

                print(
                    f"Date: {expense['Date']} | "
                    f"Category: {expense['Category']} | "
                    f"Amount: ₹{float(expense['Amount']):.2f} | "
                    f"Note: {expense['Note']}"
                )
                total_amount += float(expense["Amount"])



        if not expense_found:
            print("No expenses recorded.")

        print("----------------------------------")
        print(f"Total Amount Spent: ₹{total_amount:.2f}")

    except FileNotFoundError:
        print("Expense file not found.")


#Category-wise spending summary
def category_summary():
    print("\n=== Category Wise Summary ===")
    category_totals = {}

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                category = expense["Category"]
                amount = float(expense["Amount"])

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

        if not category_totals:
            print("No expenses recorded.")
            return

        for category, total in category_totals.items():
            print(f"{category}: ₹{total:.2f}")

    except FileNotFoundError:
        print("Expense file not found.")

# Main menu
def main():
    initialize_file()

    while True:
        print("\n================================")
        print("       EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
    else:
         print("Invalid choice! Please enter 1, 2, 3, or 4.")

# Start the program
if __name__ == "__main__":
    main()