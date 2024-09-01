stack = []
operations = int(input())
start = 0
for i in range(operations):
    action = []
    action= input().split()
    if action[0] == "PUSH":
        stack.append(action[1])
        start = start + 1
    elif action[0] == "TOP":
        if len(stack) == 0:
            print("Empty")
        else:
            print(stack[start-1])
    elif action[0] == "POP":
        if len(stack) == 0:
            print("Cannot pop")
        else:
            stack.pop(-1)
            start = start - 1
    elif action[0] == "SIZE":
        print(len(stack))