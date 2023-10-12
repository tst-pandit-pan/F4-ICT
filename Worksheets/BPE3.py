password = "f4ict"
pword = input("password?")
print()
if password == pword:
    op1 = int(input("First operand?"))
    print()
    op2 = int(input("Second operand?"))
    print()
    opr = input("Operator (+, -, *)?")
    print()
    if opr == "+": ans = op1 + op2
    if opr == "-": ans = op1 - op2
    if opr == "*": ans = op1 * op2
    print(op1, opr, op2, "=", ans)
else:
    print("Wrong password. Access Denied.")