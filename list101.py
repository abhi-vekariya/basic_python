list1 = ["dell","hp","lenovo","asus"]
print(list1)
print(list1[0:2])

#Adding in List
list1.append("iball")
print(list1)
list2 = ["logitech","zebronics","sony"]

#Update List
list2[0] = "yellow"
print(list2)

list2[1] = "cent"
print(list2)

#Delete particular name from List
del list2[0]
print(list2)

#arithmetic operator using in List
print(list1 + list2)
print(list2*2)

#max and min in List
print(max(list1))
print(min(list1))
print(len(list1))