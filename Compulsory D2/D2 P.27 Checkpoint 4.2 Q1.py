d = float(input("Please enter the diameter of the cylinder: "))
h = float(input("Please enter the height of the cylinder: "))
PI = 3.14
vol = (PI * ((d/2)**2) * h)
area = 2*PI*(d/2)*h + 2*PI*((d/2)**2)
print("The volume of the cylinder is: " + str(vol))
print("The surface area of the cylinder is: " + str(area))