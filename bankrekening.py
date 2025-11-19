class Wallet:
   def __init__(self):
       self.__balance = 0

   def __validate(self, amount):
       if amount < 0:
           raise ValueError('Amount must be positive')

   def deposit(self, amount):
       self.__validate(amount)
       self.__balance += amount

   def withdraw(self, amount):
       self.__validate(amount)
       if amount > self.__balance:
           raise ValueError('Insufficient funds')
       self.__balance -= amount

   def get_balance(self):
       return self.__balance

acct_one = Wallet()
acct_one.deposit(4) # ValueError('Amount must be positive')
print(acct_one.get_balance()) # 0

acct_one.deposit(50)
print(acct_one.get_balance()) # 50
acct_one.withdraw(-8) # ValueError('Amount must be positive')
acct_one.withdraw(58) # ValueError('Insufficient funds')