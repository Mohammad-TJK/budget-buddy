class Budget:
    def __init__(self, category):
        self.category = category
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))

    def get_expenses(self):
        return sum(amount for _, amount in self.expenses)
