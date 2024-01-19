level = int(input("How many levels (5-10)?"))
print()
print()
if (level >= 5) or (level <= 10):
    for i in range(level, 0, -1):
        for j in range(level-i):
            print("*", end="")
        for j in range(i):
            print("o", end="")
        print()