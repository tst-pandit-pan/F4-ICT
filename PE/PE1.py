form = int(input("Form(1-6)?"))
print()
if (form < 0) or (form > 6):
  print("Invalid form. Program terminated.")
else:
  classes = input("Class(A-E)?")
  print()
  if (classes == "A") or (classes == "B") or (classes == "C") or (classes == "D") or (classes == "E"):
    print("You are in F." + str(form) + classes + ".")
    if (form == 5) or (form == 6):
      if (classes == "A"):
        print("You are welcome to the talk.")
      else:
        print("You cannot join the talk.")
    else:
      print("You cannot join the talk.")
  else:
    print("Invalid class. Program terminated.")