name = ['John Chan', 'Tim Tong', 'Regina Lau', 'Danny Tsang', 'Roy Leung', "Jo Lee"]
t1mark = [] 
t2mark = []
t3mark = []
total = [0, 0, 0, 0, 0, 0]
for i in range(len(name)):
  print("Enter the three test marks for "+name[i]+" :")
  t1, t2, t3 = input().split()
  print()
  t1 = int(t1)
  t2 = int(t2)
  t3 = int(t3)
  t1mark = t1mark + [t1]
  t2mark = t2mark + [t2]
  t3mark = t3mark + [t3]
for i in range(len(name)):
  total[i] = t1mark[i] + t2mark[i] + t3mark[i]
print()
print("Students failed:")
for i in range(len(name)):
  if total[i]<150:
    print(name[i])
print()
minTotal = total[0]
min_ndx = 0
for i in range(0,len(name)):
  if total[i]<minTotal:
    minTotal = total[i]
    min_ndx = i
print( "{:<0}{:<0}{:<0.2f}{:<0}".format(name[min_ndx], ' got the lowest average mark (', minTotal/3, ')') )
