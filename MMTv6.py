#Irene Stone
#Nov 2022
#Maths Multipication Tutor v6 (MMT)
#This version should refine the previous version so that after entering the
#correct answer, the user is offered the opportunity to continue with a new
#expression. If the user enters “N” for no the application should exit. Otherwise
#the program should generate two new random number and the application should start again.

import random

n1 = random.randint(0, 12) # Generate the 1st number
n2 = random.randint(0, 12) # Generate the 2nd number
ans = n1*n2 # Calculate the product and store it in 'ans'

print("%d * %d" %(n1,n2))  # Display the expression

noTries = 1
print("Welcome!")
print("---------------------------------------------------")

while True:
    print("This is chance no ", noTries)
    usrAns = int(input("Enter your answer: ")) # Read the response
    if usrAns == ans:
        print("Correct!")
        tryAgain = input("Would you like to try again? Type Y or N \n")
        if tryAgain == "Y":
            n1 = random.randint(0, 12) # Generate the 1st number
            n2 = random.randint(0, 12) # Generate the 2nd number
            ans = n1*n2 # Calculate the product and store it in 'ans'
            print("%d * %d" %(n1,n2))  # Display the expression
            #can see where we need a function! 
        else:
            break
    else:
#        print("Incorrect! Try again")
        if usrAns > ans:
            print("Incorrect. Too high")
        else:
            print("Incorrect. Too low")
        print("---------------------------------------------------")

print("The correct answer was %d" %(n1*n2))
print("Goodbye")