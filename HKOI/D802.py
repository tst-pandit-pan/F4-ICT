N, A = input().split()
N = int(N)
A = int(A)
numbers = []
count = 0
numbers = input().split()
if A == 0:
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if int(numbers[j]) > int(numbers[j + 1]):
                tmp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = tmp
                count = count + 1
elif A == 1:
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if int(numbers[j]) < int(numbers[j + 1]):
                tmp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = tmp
                count = count + 1
print(count)
for i in range(len(numbers)):
    print(numbers[i], end=" ")
print()