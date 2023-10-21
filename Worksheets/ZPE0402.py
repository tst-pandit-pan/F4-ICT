level = 0
while (level < 5) or (level > 10):
    level = int(input("How many levels (5-10)?"))
    print()
    if (level < 5):
        print("Input at least 5 levels.")
    elif (level > 10):
        print("Input at most 10 levels.")
if (level >= 5) or (level <= 10):
    print()
    for i in range(level):
        for j in range(i):
            print(" ", end="")
        for j in range(1+2*(level-1)):
            print("o", end="")
        level = level - 1
        print()