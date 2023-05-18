list1 =['a','b','c','d']

#1st example
for i in list1:
    print(i,end =' ')

#written print for new line
print()

#2nd examplte
for i in range(1,6):
    for j in range(1,11):
        print(f"{i} x {j} = ",i * j )