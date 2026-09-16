# Name: Michael Ko
# Class: CSCI 1511
# Professor: Travis Burke 
# Date: 09/12/2026 

# Greeting message before anything happens
greeting_message = input("Hi there, you must like pizza! Click enter to continue.")
print(greeting_message)

# Statement letting user know that he/she can exit the loop/program by typing 'quit'
statement = input("Before you begin, I want to let you know that you can type 'quit' without the single quotation marks to exit the loop/program. Click enter to continue.")
print(statement)

active = True
while active:
    topping = input("Enter a pizza topping: ")

    if topping == 'quit':
        print("You have created your pizza.")
        break
    else:
        print(f"Your topping: {topping} has been added. Anything else? ")