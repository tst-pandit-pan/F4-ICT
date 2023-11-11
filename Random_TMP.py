num = [11, 12, 13, 17, 16]
print(num)
P = 1
N = len(num)
print(N)
for i in range(P, N-1):
    num[i] = num[i+1]
num[N-1] = 0
print(num)