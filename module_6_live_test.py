low=1
high=100
count=1
while True:
    guess=(low+high) // 2
    print("My guess is:",guess)
    reply=input("Enter a latter (h,l,c):").upper()
    count +=1

    if reply=="H":
        high=guess-1
    elif reply=="L":
        low=guess+1
    elif reply=="C":
        print("I guessed your number:",count,"tries!")
        break
    else:
        print("Please type H, L, or C only.")
        count -= 1


