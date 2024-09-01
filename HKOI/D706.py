queue = [0] * 10001
operations = int(input())
start = 0
end = 0
for i in range(operations):
    action = []
    action= input().split()
    if action[0] == "PUSH":
        queue[end] = action[1]
        end = end + 1
        if end == 10001:
            end = 0
    elif action[0] == "FRONT":
        if start == end:
            print("Empty")
        else:
            print(queue[start])
    elif action[0] == "POP":
        if start == end:
            print("Cannot pop")
        else:
            start = start + 1
            if start == 10001:
                start = 0
    elif action[0] == "SIZE":
        print((10001 + end - start) % 10001)