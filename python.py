#implementing the rolling dice game in python
#importing random module
import random
#Initializing variables
min_value=1
max_value=6
roll_again="yes"
#while loop
while roll_again=="yes" or roll_again=="y":
    print("dice is rolling...")
    print("the values are...")
    value1=random.randint(min_value,max_value)
    value2=random.randint(min_value,max_value)
    print(value1,value2)
    #Asking user to run the dice again or not
    roll_again=input("give input as yes or y to roll dice again ")
