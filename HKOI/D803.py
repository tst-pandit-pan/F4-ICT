N = int(input())
numbers = []        # Initialize
sorted = []         # Initialize
count = 0           # Initialize
numbers = input().split()
for i in range(N):
    for j in range(N):
        if numbers[i] > sorted[j]:
            sorted[j] = numbers[i]
            count = count + 1