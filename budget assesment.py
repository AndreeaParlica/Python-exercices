# Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and 
# entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that 
# is a list. The class should also contain the following methods:

# A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should 
# append an object to the ledger list in the form of {"amount": amount, "description": description}.
# A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. 
# If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
# A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
# A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount 
# and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with 
# the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either 
# ledgers. This method should return True if the transfer took place, and False otherwise.
# A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget 
# category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
# When the budget object is printed it should display:

# A title line of 30 characters where the name of the category is centered in a line of * characters.
# A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, 
# then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
# A line displaying the category total.
# Here is an example of the output:

# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96

# Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. 
# It should return a string that is a bar chart.

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def check_funds(self, amount):
        fund = 0
        n = len(self.ledger)
        for i in range(n):
            fund = fund + self.ledger[i]["amount"]
        if fund < amount:
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        # initialising a dictionary
        self.dep = dict()
        # adding the amount and description to dictionary
        self.dep["amount"] = amount
        self.dep["description"] = description
        # adding the deposit to ledger list
        self.ledger.append(self.dep)

    def withdraw(self, amount, description=""):
        # checking if total amount less than or greater than amount to be withdrawn
        l = self.check_funds(amount)

        if (l == True):
            self.withd = dict()
            self.withd["amount"] = -(amount)
            self.withd["description"] = description
            self.ledger.append(self.withd)
            return True
        else:
            return False

    def get_balance(self):
        fund = 0
        n = len(self.ledger)
        # retrieving the total fund in ledger
        for i in range(n):
            fund = fund + self.ledger[i]["amount"]
            return fund

    def transfer(self, amount, obname):
        objectname = obname
        a = self.withdraw(amount, f"Transfer to {objectname}")
        if a == True:
            return True
        else:
            return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" + f"{self.ledger[i]['amount']:>7.2f}" + '\n'
            total += self.ledger[i]['amount']

        output = title + items + "Total: " + str(total)
        return output



obiect_1 = Category("Food")
obiect_1.deposit(300, "haine")
obiect_1.withdraw(200, "pantofi")
obiect_1.deposit(900, "salariu")
obiect_1.transfer(300, "economii")
print(obiect_1.__str__())
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.__str__())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
