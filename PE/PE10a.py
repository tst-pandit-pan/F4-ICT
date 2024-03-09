########################################
# Name : Pan Sui Wang
# Class: 4B
# Class No.: 06
########################################

order = int(input("Input order of magic square (an 1-9 odd integer):"))         #user input
while (order < 1) or (order > 9) or ((order) % 2 == 0):
    order = int(input("Input order of magic square (an 1-9 odd integer):"))     # user input

# initialization of a 2D Python list basing on above user input (user requirement)
magic = [[0 for i in range(order)] for j in range(order)]

# print(magic)                                     # for visualization in debugging

row = 0
col = order // 2    #put 1 at the middle?
for n in range(1 , order * order + 1):
    magic[row][col] = n
    if row == 0:
        r = order - 1       #if row is 0 cannot minus row 1 again
    else:
        r = row - 1         #minus 1 from row
    if col == order - 1:
        c = 0               #if col is at the end, start from 0   
    else:
        c = col + 1         #add 1 to col
    if magic[r][c] == 0:    
        row = r
        col = c
    else:
        row = row + 1

# print(magic)                                     # for visualization in debugging

print()

for i in range(order):
    for j in range(order):
        print("{:4}".format(magic[i][j]), end="")            # print each number in a fixed-width column showing 4 characters in maximum
    print()