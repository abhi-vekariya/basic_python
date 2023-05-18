#open that file
file = open("simple_text.txt")

#read whole content of file
print(file.read())

#read only first three character
print(file.read(3))

#read line by line
print(file.readline())
print(file.readline())
print(file.readline())

#close that file
file.close()