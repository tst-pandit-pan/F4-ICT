name = ['John Chan', 'Tim Tong', 'Regina Lau', 'Danny Tsang', 'Roy Leung', "Jo Lee"]
t1mark = [0, 0, 0, 0, 0, 0]					    # Alt. ans.:  t1mark = [0, 0, 0, 0, 0, 0]
t2mark = [0, 0, 0, 0, 0, 0]					    # Alt. ans.:  t2mark = [0, 0, 0, 0, 0, 0]
t3mark = [0, 0, 0, 0, 0, 0]					    # Alt. ans.:  t3mark = [0, 0, 0, 0, 0, 0]

total = [0, 0, 0, 0, 0, 0] 						 			 

# Input marks of the 3 tests for all 6 students and add them to the list
for i in range(0, len(name)):				# for storing loop counter
    print('Enter the three test marks for', name[i] ,':')
    t1, t2, t3 = input().split()
    print()
    t1 = int(t1)
    t2 = int(t2)
    t3 = int(t3)
    t1mark[i] = t1
    t2mark[i] = t2
    t3mark[i] = t3

# Calculate the totals of the 3 tests for all 6 students 
for i in range(len(name)):
    total[i] = t1mark[i] + t2mark[i] + t3mark[i]
# Display names of those students with average mark less than 50
print()								# print a blank line
print('Students failed:');
for i in range(len(name)):
    if total[i]/3 < 50:
        print(name[i])
# Find the student with the lowest total mark 
# Assume only one student got the lowest total mark
print()									# print a blank line
minTotal = total[i]
min_ndx = 0
for i in range(len(name)):
    if total[i] < minTotal:
        minTotal = total[i]
        min_ndx = i
print("{:<0}{:<0}{:<0.2f}{:<0}".format(name[i], ' got the lowest average mark (', minTotal/3, ')'))

