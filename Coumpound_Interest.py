# Welcome Note
print("Howdy, I'm Prabindh")
# Defining  The Function
def compound_interest(P, R, T):
    # Calculates compound interest  
    Amount = P * (pow((1 + R / 100), T))  
    # Entering Through The Formula	
    CI=Amount-P
    # Printing & Returning The Simple Interest	
    print('The Compound Interest Is', CI,'Currencies')
    return CI
# Recieving The Data From The User
P=float(input("Enter The Principle : "))
T=float(input("Enter The Rate Of Interest : "))
R=float(input("Enter The Time Duration : "))
# Finding Out The Simpl Interest
compound_interest(P,R,T)