stack = []
action = input()
while action != "":
    if action.startswith("PUSH"):
        stack = 
        print(stack[-1])
    elif action == "POP":
        stack = stack.pop()
    elif action == "TOP":
        print(stack[-1])
    elif action == "SIZE":
        if len(stack) == 0:
            print("Empty")
        else:
            print(len(stack))
    action = input()