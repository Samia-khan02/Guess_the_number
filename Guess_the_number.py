import random

jackpot=random.randint(1,100)
count=0
user=int(input("Enter a number : "))

while user!=jackpot:
    if(user<jackpot):
        print("Enter higher number : ")

    else:
        print("Enter lower number : ")
    
    count+=1
    user=int(input("Enter a number : "))

print(f"Correct answer! \n You took {count} attempts to guess correctly")

