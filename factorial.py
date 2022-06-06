fact = 1 
while True: 
    answer = input ("Enter yes if you want to contiue or no if you want to quit: ").lower()
    if answer == "yes":
            number = input ("Enter a number: ")
            number = int (number)
            if number < 2:
                print ("{}!={}".format(number,1))
            else :
                for num in range (1,number+1):
                    fact = fact * num
                    
                print("{}!={}".format(number,fact))
                continue

    elif answer == "no":
        print ("Goodbye")
        quit ()
    else:
        print ("Invalid input")
        continue