class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Creating a bank account object
account1 = BankAccount("123456789", 1000)

# Accessing balance through public method
print("Initial balance:", account1.get_balance())

# Depositing and withdrawing funds
account1.deposit(500)
account1.withdraw(200)

# Accessing balance after transactions
print("Final balance:", account1.get_balance())
