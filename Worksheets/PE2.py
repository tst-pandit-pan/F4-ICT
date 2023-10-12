print("Input test marks (enter -1 to stop input):")
mark = 0
count = 0
total = 0
for i in range(1,100000):
    mark = input("Test " + str(i) + "?")
    print()
    if mark == "-1":
        print()
        break
    else:
        total = total + int(mark)
        count = count + 1
average = (total / count)
print("Number of tests = " + str(count))
print("Total mark = " + str(float(total)))
print("Average mark = " + str(average))