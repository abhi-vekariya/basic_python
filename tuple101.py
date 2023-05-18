tuple1 = ('a','b','c','d')
tuple2 = (1,2,3)

#concatination
tuple3 = tuple1 + tuple2
print(tuple3)

#indexing
print(tuple1[0])
print(tuple1[1])

#slicing
print(tuple1[0:2])

#convert list into tuple
list1 = ['hello','world','newyork']
tuple4 = tuple(list1)
print(tuple4)

#convert string into tuple
tuple5 = tuple("Hello")
print(tuple5)

#nested tuple
tuple3 = (tuple1,tuple2)
print(tuple3)

#repitation
Tuple1 = ('Geeks',) * 3
print(Tuple1)