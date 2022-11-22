#Irene Stone
#Nov 2022
#Maths Multiplication Tutor v5 (MMT)
#In this version of the application, the program should continue until the user
#gets the correct answer. Each time the user enters an answer the program continues
#to display one of the three messages, i.e. correct, too high or too low.

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