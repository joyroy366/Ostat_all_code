#first way
import math_utils

res=math_utils.add(5,7)
print(res)

res1=math_utils.subt(10,5)
print(res1)




# 2nd way
from math_utils import subt,add

res=subt(15,20)
res1=add(5,6) 
print(res)
print(res1)




# ekta folder theke file niye ase onno file run kora hoiche
import utlis.hello 

utlis.hello.say_hello("joy") #dekhar bisoy 

#2nd way
from utlis import hello

hello.say_hello("Borna")

#3rd way 
from utlis.hello import say_hello
say_hello("Sali")


import utlis


import math

res=math.gcd(5,7)
print(res)

#
import requests  

res=requests.get("https://google.com")
                
print(res.text)
