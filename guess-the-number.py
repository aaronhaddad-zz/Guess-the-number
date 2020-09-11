import random
toGuess=random.randrange(0,20,1)
while int(input())!=toGuess:
    print("Try again: ")
print("Yes you made it! The number to guess was: ",toGuess)