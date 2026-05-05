# Simple Expense Tracker

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc.): ")
    
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }
    
    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    
    print("\nYour Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['name']} - ${exp['amount']} ({exp['category']})")
    print()


def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Expenses: ${total}\n")


def menu():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


# Run the app
menu()