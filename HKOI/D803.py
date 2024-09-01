N = int(input())
count = 0
numbers = input().split()
for i in range(N):
    numbers[i] = int(numbers[i])

for i in range(N):
    key = numbers[i]
    j = i - 1
    while j >= 0 and key < numbers[j]:
        numbers[j + 1] = numbers[j]
        j = j - 1
    numbers[j + 1] = key
    count = count + 1
    for k in range(count):
        print(numbers[k], end = " ")
    print()