print("Input test marks (enter -1 to stop input):")
mark = 0
count = 0
total = 0
while mark != -1:
    mark = int(input("Test " + str(count + 1) + "?"))
    print()
    if mark != -1:
        count = count + 1
        total = total + int(mark)
print()
average = (total / count)
print("Number of tests = " + str(count))
print("Total mark = " + str(float(total)))
print("Average mark = " + str(average))