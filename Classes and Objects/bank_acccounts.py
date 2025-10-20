class BankAccount:
    def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self,deposit):
        self.balance += deposit
        return self.balance
     
    def withdraw(self,withdraw):
        self.balance -= withdraw
        return self.balance
    
    def display_balance(self):
        print("Current Balance: $",self.balance)

BankAccount1 = BankAccount("Isuranga","Jayassri",1337134,"Savings",4563,0.0)

BankAccount1.deposit(96)

BankAccount1.withdraw(25)

BankAccount1.display_balance()

    