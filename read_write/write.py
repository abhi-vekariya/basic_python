with open('text.txt') as reader:
    line_list = reader.readlines()
    reversed_list = reversed(line_list)
    with open('text.txt','w') as writer:
        for item in reversed_list:
            writer.write(item)





