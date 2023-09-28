name = input("Please enter your name: ")
test1 = int(input("Please enter the first test result: "))
test2 = int(input("Please enter the second test result: "))
exam = int((input("Pleae enter the exam result: ")))

TEST1_WEIGHT = 0.2
TEST2_WEIGHT = 0.3
EXAM_WEIGHT = 0.5

overall = (test1*TEST1_WEIGHT+test2*TEST2_WEIGHT+exam*EXAM_WEIGHT)/(TEST1_WEIGHT+TEST2_WEIGHT+EXAM_WEIGHT)

print(name, end ="")
print(", your overall result of ICT is:", str(overall))