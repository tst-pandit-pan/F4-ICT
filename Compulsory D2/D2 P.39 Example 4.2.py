a = float(input("Enter number 1:"))
b = float(input("Enter number 2:"))
c = float(input("Enter number 3:"))
d = float(input("Enter number 4:"))

if a < b:
	min = a
else:
	min = b
if c < min:
    min = c
if d < min:
    min = d
