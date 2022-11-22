#Irene Stone
#Nov 2022
#Extension exercise
#User is asked how many sides and then the shape is drawn

from turtle import *

howManySides = int(input("How many sides? \n"))

for i in range(howManySides):
    forward(100)
    left(360/howManySides)