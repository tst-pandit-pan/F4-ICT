N, Q = input().split()
N = int(N)
Q = int(Q)
num_list = []               ##List of numbers exists
num_list = input().split()
for i in range (N):
    num_list[i] = int(num_list[i])
check_list = []             ##List of numbers to be checked
check_list = input().split()
for i in range (Q):
    check_list[i] = int(check_list[i])
#Input Done

for i in range (Q):
    ##Intialize
    found = False
    start = 0
    end = N-1
    mid = (start + end) // 2
    ##Check
    while (start <= end) and (found == False):
        if check_list[i] == num_list[mid]:
            found = True
        elif check_list[i] > num_list[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2
    ##Output
    if found == True:
        print("Yes")
    else:
        print("No")