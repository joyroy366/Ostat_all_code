#Exception Handeling

#a="ABC"
#b=int(a)
#print(type(b))
#list index error

#Try to Catch error
try:
   a=int(input("Enter number a:"))
   b=int(input("Enter number b:"))
   print(f"Sum is {a+b}")
except:
   print("place Enter number")

# onno error
try:
    a=int(input("Enter number a:"))
    b=int(input("Enter number b:"))

    print("Result is :",a/b)
except ValueError:
   print("bhai number den bhai")
except ZeroDivisionError:
   print("bhai b ar value 0 hoi na")
except Exception as e:
   print(e)
   print("ki hoise ami nijei jani na!")

#File Handeling


#Mystery of Path