"""
Create a class called Account which will be an abstract class for three other classes called CheckingAccount, SavingsAccount and BusinessAccount. Manage credits and debits from these accounts through an ATM style program.
"""

class Account(object):
	"""
	An Abstract base class representing a Bank Account.
	"""
	def __init__(self, init_balance=0):
		self.balance = init_balance
		
	def deposit(self, amount):
		self.balance += amount
	
	def withdraw(self, amount):
		self.balance -= amount
		
	def overdrawn(self):
		return self.balance < 0
	
"""
class CheckingAccount:
	def __init__(self):
		
class SavingsAccount:
	def __init__(self):
		
	
class BusinessAccount:
	def __init__(self):
"""		

	
my_account = Account(15)
my_account.withdraw(5)
print my_account.balance