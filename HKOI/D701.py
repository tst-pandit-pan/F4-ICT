queue = []
operations = int(input())
start = 0
end = 0
for i in range(operations):
    action = []
    action= input().split()
    if action[0] == "PUSH":
        queue.append(action[1])
        end = end + 1
    elif action[0] == "FRONT":
        if len(queue) == 0:
            print("Empty")
        else:
            print(queue[start])
    elif action[0] == "POP":
        if len(queue) == 0:
            print("Cannot pop")
        else:
            queue.pop(start)
    elif action[0] == "SIZE":
        print(len(queue))