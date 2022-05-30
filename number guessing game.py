import random
from tkinter import TRUE
top_of_range=input("\r Enter a number: ")
gusses=0
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    
else:
    print("\r Please enter a number next time")
    quit()

if top_of_range==0:
    print("\r Please enter a number larger than zero next time.")
    quit()

random_number=random.randint(0,top_of_range)
while TRUE:
    gusses+=1
    user_guess=input("\n Enter your guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("\n Please enter a number as your guess next time")
        quit()
    if user_guess==random_number:
        print("\n You got it right!!")
        break
    else:
        if user_guess<random_number:
            print("\n Enter a larger number")
        else:
            print("\n Enter a smaller number")
print("You got it in",gusses,"guesses")




    