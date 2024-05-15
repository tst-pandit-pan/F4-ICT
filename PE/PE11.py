# PE11 - Arithmetic Drilling

# **************************************************
# Enter your personal information below
# Name: {Pan Sui Wang}
# Class: F.4{B}
# Class Number: {06}
# **************************************************

# program ArithmeticDrill

# List of variables to be used:
#  choice stores single-character user's choice
#  correct_answer stores answer
#  user_answer stores user's answer
#  qcount     counts number of questions attempted
#  ncorrect  counts number of questions correctly answered

import random
# import os
# from os import system, name
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
    choice = int(input("Enter your choice: "))
    while (choice < 0) and (choice > 6):
        if (choice < 1) or (choice > 5):
            print("Invalid input. Reenter using 1-5 ")
        choice = int(input("Enter your choice: "))
    print()


# Each of the 4 following subprograms below displays a question on the screen
# and stores the answer to the question to the variable correct_answer

def addition():    # may use x and y as local variables
    global correct_answer
    global x, y
    x = int(random.random()*100)
    y = int(random.random()*100)
    correct_answer = x + y

def subtraction():     # may use x and y as local variables
    global correct_answer
    global x, y
    x = int(random.random()*100)
    y = int(random.random()*100)
    while x < y:
        y = int(random.random()*100)
    correct_answer = x - y

def multiplication():    # may use x and y as local variables
    global correct_answer
    global x, y
    x = int(random.random()*12)
    y = int(random.random()*12)
    correct_answer =  x * y

def division():           # may use x and y as local variables
    global correct_answer
    global x, y
    x = int(random.random()*12)           # generate quotient first
    y = int(random.random()*12)           # generate divisor
    correct_answer = x / y

# using CASE statement, call a procedure to generate a question according to the user's choice
def generate_question():
    user_answer = 0
    match choice:
        case 1 :
            addition()
        case 2 :
            subtraction()
        case 3 :
            multiplication()
        case 4 :
            division()
        # fill in a few missing lines here

# accept user's answer into the global variable user_answer and respond accordingly
def accept_answer():
    global user_answer
    global correct_answer
    user_answer = int(input())
    print()
    if user_answer == correct_answer:
        print('You are right. Good!')
    else:
        print("Sorry! you are wrong.")
        print("The correct answer is " + str(correct_answer) + ".")
    print()

# record data for statistics into the global variables qcount and ncorrect
def statistics():
    # fill in a few missing lines here
    global qcount, ncorrect
    qcount = qcount + 1
    if user_answer == correct_answer:
        ncorrect = ncorrect + 1

# use an empty loop to create a time delay
def delay():      # use local variable i
    # for i in range(333333333):            # time delay loop
        # pass
    sleep(1)                                 # 1 seconds

def display_statistics():
    global qcount
    global ncorrect
    print('Thank you for using this drilling program.')
    print('You got ', end="")
    print(ncorrect/qcount, end="")
    print(" '% correct.")

# Main program
choice = 0             # initialize a value to global variable choice
qcount = 0                # initialize a value to global variable qcount
user_answer = 0         # initialize a value to global variable user_answer
correct_answer = 0        # initialize a value to global variable correct_answer
ncorrect = 0              # initialize a value to global variable ncorrect
menu()
while (choice != 5):
    generate_question()
    accept_answer()
    if (choice >= 1) and (choice <= 4):
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