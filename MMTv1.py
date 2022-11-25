#Irene Stone
#Nov 2022
#Maths Multiplication Tutor v1 (MMT)
#This is a basic version provided above. The computer generates two random numbers and
#prompts the user to enter their product. If the user’s answer is correct the program
#displays a message.

import random

n1 = random.randint(0, 12) # Generate the 1st number
n2 = random.randint(0, 12) # Generate the 2nd number
ans = n1*n2 # Calculate the product and store it in 'ans'

print(n1, "*", n2)       # Display the expression
usrAns = int(input("Enter your answer: ")) # Read the response

# Evaluate the condition
if usrAns == ans:
   print("Correct!")

print("The correct answer was %d" %(n1*n2))
print("Goodbye")
