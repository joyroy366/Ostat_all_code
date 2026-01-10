class Student:
    name="A" #property
    roll=1   #class variable
    marks=0

    def add_mark(self):  #Method
        self.marks+=5

#object creat
o1=Student() #Object or Instance
o2=Student()

o1.name ="Tusar"
print(o1.name)
print(o2.name)

o1.add_mark()
o1.add_mark()


#Constructor /spesal class 

class BankAccount:
    def __init__(self):
        self.ower="abc" #Instance Variable
        self.balance=2000
        
ac1=BankAccount()
print(ac1.ower)




class BankAccount:
    def __init__(self,name,balance):
        self.ower=name #Instance Variable
        self.balance=balance
        
ac1=BankAccount("Tusar",500)
ac2=BankAccount("Zayed",1500)
print(ac1.ower)
print(ac1.balance)




class BankAccount:
    def __init__(self,name):
        self.ower=name #Instance Variable
        self.balance=0

    def deposit(self,amount)
        self.balance=self.balance + amount
        print(f"{self.balance} _ Balance")
        
ac1=BankAccount("Tusar")
ac2=BankAccount("Zayed")
print(ac1.ower)
print(ac1.balance)




