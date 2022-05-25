print("Welcome to my computer quiz!")
response= input("\nDo you want to play the game? ").lower()
score=0
result=True
if response !="yes":
    quit()
else:
    print("Okay let's play😁. Good luck!")

answer=input("What does GUI stand for in Computer System? ").lower()
if answer == "graphical user interface":
    print ("Correct")
    score+=1
else:
    print("Incorrect!!!")

answer=input("What does CLI stand for in Computer System? ").lower()
if answer == "command line interface":
    print ("Correct")
    score += 1
else:
    print("Incorrect!!!")

answer=input("What does MS stand for in Computer System? ").lower()
if answer == "microsoft":
    print ("Correct")
    score += 1
else:
    print("Incorrect!!!")

answer=input("What does PS stand for in Computer System? ").lower()
if answer == "power supply":
    print ("Correct")
    score += 1
else:
    print("Incorrect!!!")

answer=input("What does CPU stand for in Computer System? ").lower()
if answer == "central processing unit":
    print ("Correct")
    score += 1
else:
    print("Incorrect!!!")

print("You got",score,"/5 questions")
print ("You got ",(score/5)*100 , "%")

if score>=3:
    print("You have passed the quiz.")
else:
    result=False
    print("fail")


