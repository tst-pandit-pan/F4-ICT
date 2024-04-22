########## THIS CODE GENREATED BY GOOGLE GEMINI 1.5 PRO ##########
# PE11 - Arithmetic Drilling# **************************************************# Enter your personal information below# Name: {Chan Tai Man ?????}# Class: F.4{A/B/D ?????}# Class Number: {99 ??????}# **************************************************# program ArithmeticDrill# List of variables to be used:#  choice stores single-character user's choice#  correct_answer stores answer#  user_answer stores user's answer#  qcount     counts number of questions attempted#  ncorrect  counts number of questions correctly answered
import random
# import os# from os import system, name
from time import sleep

# display menu; accept and validate choice
def menu():
    global choice
    print('--- MENU ---')
    print()
    print('1 : Addition')
    print('2 : Subtraction')
    print('3 : Multiplication')
    print('4 : Division')
    print('5 : Quit')
    print()
    choice = input('Your choice: ')
    while choice not in ['1', '2', '3', '4', '5']:
        if not choice.isdigit():
            print('Invalid input. Please enter a number.')
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')
        choice = input('Your choice: ')
    print()

# Each of the 4 following subprograms below displays a question on the screen
# and stores the answer to the question to the variable correct_answer
def addition():
    # may use x and y as local variables
    global correct_answer
    x = int(100 * random.random()) + 1  # Generate random integer between 1 and 100
    y = int(100 * random.random()) + 1
    print(x, ' + ', y, ' = ', end="")  # end="" prevents newline
    correct_answer = x + y

def subtraction():
     # may use x and y as local variables
    global correct_answer
    x = int(100 * random.random()) + 1
    y = int(100 * random.random()) + 1
    while x < y:  # Ensure x is greater than y for positive difference
        y = int(100 * random.random()) + 1
    print(x, ' - ', y, ' = ', end="")
    correct_answer = x - y

def multiplication():
    # may use x and y as local variables
    global correct_answer
    x = int(20 * random.random()) + 1  # Generate random integer between 1 and 20
    y = int(20 * random.random()) + 1
    print(x, ' x ', y, ' = ', end="")
    correct_answer =  x * y

def division():
           # may use x and y as local variables
    global correct_answer
    quotient = int(20 * random.random()) + 1  # Generate quotient first
    divisor = int(20 * random.random()) + 1   # Generate divisor
    x = quotient * divisor
    y = divisor
    print(x, ' / ', y, ' = ', end="")
    correct_answer = quotient

# using CASE statement, call a procedure to generate a question according to the user's choice
def generate_question():
    user_answer = 0
    match choice:
        case '1':
            addition()
        case '2':
            subtraction()
        case '3':
            multiplication()
        case '4':
            division()
        # fill in a few missing lines here

# accept user's answer into the global variable user_answer and respond accordingly
def accept_answer():
    global user_answer
    try:
        user_answer = int(input())
        print()
        if user_answer == correct_answer:
            print('You are right. Good!')
        else:
            print('The correct answer is ', correct_answer)
    except ValueError:
        print("Invalid input. Please enter a number.")
    print()

# record data for statistics into the global variables qcount and ncorrect
def statistics():
    global qcount, ncorrect
    qcount += 1  # Increment question count
    if user_answer == correct_answer:
        ncorrect += 1  # Increment correct answer count 

# use an empty loop to create a time delay
def delay():
      # use local variable i
    # for i in range(333333333):
            # time delay loop
        # pass
    sleep(1)                                 # 1 seconds

def display_statistics():
    if qcount != 0:
        percent_correct = (ncorrect / qcount) * 100
        print('Thank you for using this drilling program.')
        print('You got ', end="")
        print(f"{percent_correct:.1f}", end="")  # Format percentage with one decimal place
        print(" '% correct.")

# Main program
choice = 0             # initialize a value to global variable choice
qcount = 0                # initialize a value to global variable qcount
user_answer = 0         # initialize a value to global variable user_answer 
# ... (rest of the code from previous response)

correct_answer = 0        # initialize a value to global variable correct_answer
ncorrect = 0              # initialize a value to global variable ncorrect
menu()
while (choice != '5'):  # Use '5' for string comparison
    generate_question()
    accept_answer()
    if (choice >= 1) and (choice <= 4):  # Use '1' to '4' for string comparison
        statistics()
    delay()
    print("\n" * 100)    # clear screen
    menu()
if qcount != 0:
    display_statistics()
else:
    print("Statistics will only be shown for at least one question completed.")
print()
print('Press ENTER to end program')
temp = input()