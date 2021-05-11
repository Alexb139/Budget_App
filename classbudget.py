class Category:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # Methods
    def deposit(self, amount):
        return "This is a deposit method"

    def check_balance(self, amount):
        return "This is a check balance method"

    def withdraw(self, amount):
        return "This is a withdraw method"

    def transfer(self, amount):
        # Transfer money from one category to another category
        return "This is a transfer method"

category_clothing = Category("Clothing", 100)
category_food = Category("Food", 150)
category_entertainment = Category("Entertainment", 50)
category_rent = Category("Rent", 1400)
category_pet = Category("Pet", 100)
category_insurance = Category("Insurance", 200)


print(category_clothing.deposit())
print(category_clothing.check_balance())
print(category_clothing.withdraw())
print(category_clothing.transfer())
