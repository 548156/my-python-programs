import math
def simple_interest(p,r,t):
    si=p * r *t/100
  
    return si
p=int(input("Enter the principal amount: "))
r=int(input("Enter the rate: "))
t=int(input("Enter the number of years: "))
print(" The simple interest ",simple_interest(p,r,t),)

def compound_interest(p,r,t):
    amount = p*pow((1+r/100) ,t)
    ci= amount -p
    return ci

print("The compound interest is",compound_interest(p,r,t))