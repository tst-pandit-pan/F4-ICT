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
col = order // 2
for n in range(1, order * order + 1):
    magic[row][col] = n
    if row == 0:
        r = order - 1
    else:
        r = row - 1
    if col == order - 1:
        c = 0
    else:
        c = col + 1
    if magic[r][c] != 0:
        row += 1
    else:
        row = r
        col = c

# print(magic)                                     # for visualization in debugging

print()

for i in range(order):
    for j in range(order):
        print("{:4}".format(magic[i][j]), end="")            # print each number in a fixed-width column showing 4 characters in maximum
    print()