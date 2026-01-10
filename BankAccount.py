class BankAccount:
    def __init__(self,name):
        self.ower=name #Instance variable / Object variable
        self.balance=0

    def check_balance(self):
        print(f"Account Ower :{self.ower} - Balance: {self.balance}")
    
    def deposit(self,amont):
        self.balance +=amont
        print(f"{amont} TK added to {self.ower}'s Account")

    def withdraw(self,withdrawamont):
        if self.balance >=withdrawamont:
            self.balance-=withdrawamont
            print(f"{withdrawamont} Tk withdraw to {self.ower}'s account")
        else:
            print(f"Sorry {self.ower} do not enough the balance {withdrawamont} ")

    def AccountInfo(self):
        print(f"Account Ower :{self.ower}")


abc=BankAccount("Zayed")
print(abc.ower)
print(abc.balance)
abc.check_balance()
abc.deposit(450)

abc1=BankAccount("Borna")
abc1.AccountInfo()
abc1.balance=550
abc1.check_balance()
abc1.deposit(450)
abc1.withdraw(1100)
abc1.withdraw(900)
abc1.check_balance()

abc.check_balance()
