import random

n = [0, 0, 0, 0, 0, 0, 0]
sn = [0, 0, 0, 0, 0, 0]

# Generate 49 non repeat numbers
for i in range(len(n)):
    n[i] = random.randint(1, 49)
    while n[i] in n[:i]:                #Check the current generated num exists in the previously generated num of the list
        n[i] = random.randint(1, 49)    #Generate again if exists

# Sort the numbers in ascending order
for i in range(len(sn)):
    min = n[0]      #Initialize the minimum value
    pmin = 0      #Initialize the position of the minimum value
    for j in range(1, len(sn)):
        if n[j] < min:
            min = n[j]
            pmin = j
    sn[i] = min
    n[pmin] = 50

#Print numbers generated
print('The six drawn numbers are ', end = '')
for i in range(len(sn)):
    print(sn[i], end = '')
    if i != 5:
        print(', ', end = '')
    else:
        print()
        print('The extra-number is ' + str(n[6]) + '.')
