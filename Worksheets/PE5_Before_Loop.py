import random
answer = int(random.random() * 100)
print('[ Guess a number from 1 to 100 ]')
guess = int(input("Your guess: "))
while (guess != answer):
    if (guess < answer):
        print("--- Too small")
    elif (guess > answer):
        print("--- Too big")
    guess = int(input("Your guess: "))
print("--- Bingo! You have got it.")
print('[ Press ENTER to end program. ]')
key = input()