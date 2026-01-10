#Funtions
def say_bye():
    print("Hahaha! Bye!")
def say_hello():
    print("Hi")
    print("Hello")
    say_bye()

print("Welcome")
say_hello()
print("blablabla")
say_hello()

def fine_area(radius):#perameter
    area=3014159*(radius**2)# area is a call stock
    return area

xyz=fine_area(5) #argument

print(xyz)

#                     lamda funtion
#def calc_area(r):
#     return 3.1416*r**2
calc_area=lambda r:3.1416*r**2

print(calc_area(5))


#Decorator Function

def add_cream(func):
    def wrapper():
      print("Making Speacial Cream Wala Food!")
      func()
      print("Add cream on top!")
    return wrapper

@add_cream
def make_coffee():
    print("Making plan coffee")

@add_cream
def make_cake():
    print("Making valina cake")

make_coffee()
make_cake()

#Genaretor



