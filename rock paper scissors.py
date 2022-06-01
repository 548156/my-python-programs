import random

user_wins=0
computer_wins=0
gueses=["rock","paper","scissors"]
while True:
    user_answer=input("Enter rock/ paper/ scissors or Q if you want to quit: ").lower()

    if user_answer=="q":
        break

    if user_answer not in gueses:
        print("Invalid input")
        continue

    random_number=random.randint(0,2)
    computer_guess=gueses[random_number]
    print("computer picked",computer_guess)
    if user_answer==computer_guess:
        print("Neither won")

    elif user_answer=="rock" and computer_guess=="scissors":
            print("You win!")
            user_wins+=1
    elif user_answer=="paper" and computer_guess=="rock":
        print("You win!")
        user_wins+=1
    elif user_answer=="scissors" and computer_guess=="paper":
        print("You win!")
        user_wins+=1
    else:
        print("You Loose!")
        computer_wins=+1


print("You won",user_wins,"times")
print("The computer won",computer_wins,"times")
print("See you again next time!!🖐🖐🖐")

