
import random

minnumber = 0
maxnumber = 500
secretnumber = random.randint(minnumber,maxnumber)
question = input(" ")
while question != secretnumber:
    
    question = int(input(f'Choose a number between {minnumber} and {maxnumber} '))
    
    
    try:
        if secretnumber > int(question):
            print(f"The number is larger than {question}")
        elif secretnumber < int(question):
            print(f"The number is less than {question}")
        else: 
            print(f"Congrats! The final number was {secretnumber}!")
            break
    except ValueError:
        print("Please enter an integer that has no decimals.")
        

