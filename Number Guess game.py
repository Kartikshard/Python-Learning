import random

x= int(random.randrange(1,3))
print("Please Enter Your Number : ")
yourNumber=int(input())
if yourNumber==x:
    print("You win")
else:
        print("loose")
print(f"right answer {x}")