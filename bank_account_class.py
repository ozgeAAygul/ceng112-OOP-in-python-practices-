# Task 3: Create a BankAccount class with deposit, withdraw, and balance check methods.
class BankAccount:
  def __init__(self, owner, balance):
    self.owner = owner
    self.__balance = balance

  def deposit(self, amount):
    if not amount:
      print("Invalid input.")
      return
    if not type(amount) == int:
      try:
        amount = int(amount)
      except ValueError:
        print("Invalid input.")
        return
    if amount > 0:
      self.__balance += amount
      print("Money deposited.")
    else:
      print("Invalid input.")

  def witdraw(self, amount):
    if not amount:
      print("Invalid input.")
      return
    
    if not type(amount) == int:
      try:
        amount = int(amount)
      except ValueError:
        print("Invalid input.")
      return
    if amount > 0 :
      if self.__balance > amount :
        self.__balance -= amount
        print("Transaction successful.")
      else:
        print("Insufficient funds.")
    else:
      print("Invalid input.")

  def getBalance(self):
    print(self.__balance)

p1 = BankAccount("Özge", 2000)
p1.deposit(800)
p1.deposit("100")
p1.getBalance()


    