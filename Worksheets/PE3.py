print("{:<}{:^5}{:^9}{:^8}{:^8}{:^8}{:^8}{:^8}".format("\\rate(%)", "3", "4", "5", "6", "7", "8", "9"))
print("year---------------------------------------------------------")
for i in range(20):
    year = i + 1
    print("{:>3}".format(year), end = "")
    #print the year
    print("{:>3}".format(":"), end = "")
    #print the colon
    for j in range(3,10):
        amount = 100 * (1 + j / 100) ** year
        #calculate the amount get after interest given, replace 100 with input if needed
        print("{:^8.2f}".format(amount), end = "")
    print()