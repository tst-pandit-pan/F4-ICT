import random
# Initialization
n = [0, 0, 0, 0, 0, 0, 0]
sn = [0, 0, 0, 0, 0, 0]

# Generating 7 non-repeating numbers between 1 and 49
n[0] = int(random.random() * 49) + 1
exist = False
for i in range(1,?):
    while exist:
      n[i] = ?(random.random() * ?) + 1
      exist = ?
      j = 0
      while (j <= ?) ? not exist:
          if ? :   # check the current generated num exists in the previously generated num of the list
              exist = True
          ?
    ?									# the most challenging one

# Sort the numbers in ascending order
for i in range(?):
    min = n[0]
    pmin = 0
    for j in range(1,?):
        if ? :
            min = ?
            pmin = ?
    sn[i] = ?     # copy the minimum value of round i to the new array sn[]
    n[pmin] = ?   # assign a value big enough so that the num copied to sn[] will not be minimum anymore

# Displaying the numbers generated
print("The six drawn numbers are ", end = "")
for i in range(?):
    print(?, end = "")
    if i != ?:
        print(", ", end = "")
    else:
        print(?)
        print("The extra-number is " + int(n[?]) + ".")