# PE10 - A Hand Of Cards

# **************************************************
# Enter your personal information below
# Name: {Pan Sui Wang}
# Class: F.4{B}
# Class Number: {06}
# **************************************************

import random
# Initialize all elements of 2D array of Card to 0
card = [ [0], [0], [0], [0] ]
for i in range(4):
    card[i] = [-9,0,0,0,0,0,0,0,0,0,0,0,0,0]
# print(card)             # for visualization in debugging

# Initialize 1D array of SuitCount to 0
SuitCount = []
for i in range(4):
  SuitCount = SuitCount + [0]

# Generate 5 different cards
# Generate a random number 0 to 3
x = int(random.random() * 3)
# Generate a random number 1 to 13
y = int(random.random() * 13)
card[x][y] = 0
count = 0
while count < 5:
    x = int(random.random() * 4)
    y = int(random.random() * 13)
    if card[x][y] == 0:
        card[x][y] = 1
        count = count + 1

print()

# Display the hand of card
print('*** Your hand of cards ***')
for x in range(4):
    for y in range(1,14):
        if card[x][y] == 1:
            match x:
                # Fixed width of 9 characters with LEFT-alignment for printing the name of each suit in 1st column
                case 0 : print("{:<9}".format('Spade'), end = "")
                case 1 : print("{:<9}".format('Heart') , end = "")
                case 2 : print("{:<9}".format('Club') , end = "")
                case 3 : print("{:<9}".format('Diamond') , end = "")
            match y:
                case 1 : print('A')
                case 11 : print('J')
                case 12: print('Q')
                case 13: print('K')
                case _: print(str(y))

print()

# Count no. of cards in each suit
for i in range(4):
    for j in range(1,14):
        if card[i][j] == 1:
            SuitCount[i] = SuitCount[i] + 1
for i in range(4):
    if SuitCount[i] !=  0:
        print('# of ', end="")
        match x:
          case 0 : print('Spade', end = "")
          case 1 : print('Heart', end = "")
          case 2 : print('Club', end = "")
          case 3 : print('Diamond', end = "")
        print(' cards =',SuitCount[i])