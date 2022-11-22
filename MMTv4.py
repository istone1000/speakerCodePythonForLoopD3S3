#Irene Stone
#Nov 2022
#Maths Multipication Tutor v4 (MMT)
#This is the same as version 3 except that the program should use a
#while loop to give the user at most three chances to get the correct answer.

import random

n1 = random.randint(0, 12) # Generate the 1st number
n2 = random.randint(0, 12) # Generate the 2nd number
ans = n1*n2 # Calculate the product and store it in 'ans'

print("%d * %d" %(n1,n2))  # Display the expression

noTries = 1
print("Welcome! You have 3 chances to get the right answer")
print("---------------------------------------------------")

while noTries < 4:
    print("This is chance no ", noTries)
    usrAns = int(input("Enter your answer: ")) # Read the response
    if usrAns == ans:
        print("Correct!")
        break
    else:
        print("Incorrect!")
        if usrAns > ans:
            print("Too high")
        else:
            print("Too low")
        print("---------------------------------------------------")
    noTries = noTries + 1

print("The correct answer was %d" %(n1*n2))
print("Goodbye")