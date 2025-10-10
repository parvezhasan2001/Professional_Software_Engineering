#Week-11
#Activity-2

import unittest

class Expense:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description):
        expense = Expense(amount, description)
        self.expenses.append(expense)

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)
    
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense(50, "Groceries")
    tracker.add_expense(20, "Transport")
    print(f"Total Expenses: ${tracker.total_expenses()}")


import unittest

class TestExpenseTracker(unittest.TestCase):
    def test_add_and_calculate_total_expense(self):
        tracker = ExpenseTracker()
        tracker.add_expense(50, "Groceries")
        tracker.add_expense(20, "Transport")
        self.assertEqual(tracker.total_expenses(), 70)
        
if __name__ == "__main__":
    unittest.main()