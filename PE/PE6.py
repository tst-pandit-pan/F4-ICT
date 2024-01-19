import random

throw = True

print("*** DICE GAME ***")
print("Press any key to continue rolling")
print()
print("<1>  <2>  <3>", end='')
while throw == True:
    x = input()					# collect a dummy key input only
    d1 = int(6*random.random())    # generate a random integer from 1 to 6 for dice 1
    d2 = int(6*random.random())    # generate a random integer from 1 to 6 for dice 2
    d3 = int(6*random.random())    # generate a random integer from 1 to 6 for dice 3
    print("{:>2}{:>5}{:>5}".format(d1,d2,d3), end='')
    if (d1<d2) and (d2<d3):
        print()
        print("You won.")
        throw == False
    elif (d1==d2) and (d2==d3):
        print()
        print("Game Drew.")
        throw == False
    elif (d1>d2) and (d2>d3):
        print()
        print("Computer won.")
        throw == False