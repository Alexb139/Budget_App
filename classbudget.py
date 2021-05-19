class Category:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # Methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited ${} in {} category. Your current balance is {}".format(amount, self.category, self.amount)

    def check_balance(self, amount):
        if self.amount > amount: 
            return True
        else:
            return False

    def withdraw(self, amount):
        self.amount -= amount 
        return "You have successfully withdrawn ${} in {} category. Your current balance is {}".format(amount, self.category, self.amount)

    def transfer(self, amount, category):
        # Transfer money from one category to another category
        if not self.check_balance(amount):
            return "Transfer not successful"

        self.amount -= amount
        category.amount += amount
        return "You have transferred ${} to {} category".format(amount, category.category)


category_clothing = Category("Clothing", 100)
category_food = Category("Food", 150)
category_entertainment = Category("Entertainment", 50)
category_rent = Category("Rent", 1400)
category_pet = Category("Pet", 100)
category_insurance = Category("Insurance", 200)


print(category_clothing.deposit(50))
print(category_clothing.check_balance(100))
print(category_clothing.withdraw(25))
print(category_clothing.transfer(20, category_entertainment))

