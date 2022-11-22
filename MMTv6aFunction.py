#Irene Stone
#Nov 2022
#Maths Multipication Tutor v6a (MMT)
#using a Function

import random
import os
 
def MMT():
    a = random.randint(0, 12) # Generate the 1st number
    b = random.randint(0, 12) # Generate the 2nd number
    ans = a*b  #Calculate the product and store it in 'ans'
    print("%d * %d" %(a,b))  # Display the expression
    return (ans)

print("Welcome!")
print("---------------------------------------------------")
ans = MMT()

while True:
    usrAns = int(input("Enter your answer: ")) # Read the response
    if usrAns == ans:
        print("Correct!")
        print("---------------------------------------------------")
        tryAgain = input("Would you like to try again? Type Y or N \n")
        
        if tryAgain.upper() == "Y":
#            os.system('clear')   # try it in thonny
            print("-------------------New Game...Good Luck!----------------------")
            ans = MMT()
        else:
            break
    else:
#        print("Incorrect! Try again")
        if usrAns > ans:
            print("Incorrect. Too high")
        else:
            print("Incorrect. Too low")
        print("---------------------------------------------------")

print("Goodbye")