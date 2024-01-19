import random
answer = random.randint(1, 100)
print("[ Guess a number from 1 to 100 ]")
guess = 0
while (guess != answer):
	guess = int(input("Your guess: "))
	if (guess < answer):
		print("--- Too small")
	elif (guess > answer):
		print("--- Too big")
else:
	print("--- Bingo! You have got it.")
print("[ Press ENTER to end program. ]")
key = input()