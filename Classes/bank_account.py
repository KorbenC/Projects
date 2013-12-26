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
	
class checking_Account(Account):
	def __init__(self,checking_init=0):
		self.balance = checking_init

class savings_Account(Account):
	def __init__(self, savings_init=0):
		self.balance = savings_init

my_account = Account(20)
my_checking_account = checking_Account(15)
my_savings_account = savings_Account(25)
my_account.withdraw(5)
my_checking_account.withdraw(10)
my_savings_account.deposit(1)
print 'checking: %d' %my_checking_account.balance
print 'Account: %d' %my_account.balance
print 'Savings: %d' %my_savings_account.balance