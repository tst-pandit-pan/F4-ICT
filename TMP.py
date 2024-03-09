import random

# PE10 - A Hand Of Cards

# **************************************************
# Enter your personal information below
# Name: {Chan Tai Man}
# Class: F.4{A/B/D}
# Class Number: {99}
# **************************************************


# Initialize all elements of 2D array of Card to 0
card = [[-9,0,0,0,0,0,0,0,0,0,0,0,0,0] for _ in range(4)]

# Initialize 1D array of SuitCount to 0
SuitCount = [0 for _ in range(4)]

# Generate 5 different cards
count = 0
while count < 5:
    x = int(random.random() * 4)
    y = random.randint(1, 13)
    if card[x][y] == 0:
        card[x][y] = 1
        count += 1

print()

# Display the hand of card
print('*** Your hand of cards ***')
for i in range(4):
    for j in range(1, 14):
        if card[i][j] == 1:
            suit = ''
            value = ''
            if i == 0:
                suit = 'Spade'
            elif i == 1:
                suit = 'Heart'
            elif i == 2:
                suit = 'Club'
            elif i == 3:
                suit = 'Diamond'
            
            if j == 1:
                value = 'A'
            elif j == 11:
                value = 'J'
            elif j == 12:
                value = 'Q'
            elif j == 13:
                value = 'K'
            else:
                value = str(j)
            
            print('{:<9}{}'.format(suit, value))

print()

# Count no. of cards in each suit
for i in range(4):
    for j in range(1, 14):
        if card[i][j] == 1:
            SuitCount[i] += 1

for i in range(4):
    if SuitCount[i] > 0:
        print('# of', end=" ")
        if i == 0:
            print('Spade', end=" ")
        elif i == 1:
            print('Heart', end=" ")
        elif i == 2:
            print('Club', end=" ")
        elif i == 3:
            print('Diamond', end=" ")
        print('cards =', SuitCount[i])
