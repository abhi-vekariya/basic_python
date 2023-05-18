file = open("simple_text.txt")

#Using 'filereadline()' method
# read_start = file.readline()
# while read_start != "":
#     print(read_start)
#     read_start = file.readline()

#Using 'filereadlines()' method
for sentence in file.readlines():
    print(sentence)

file.close()