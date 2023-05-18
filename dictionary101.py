my_dict = {
    "paresh":10,
    "mahesh":20,
    "mukesh":30
}

print(my_dict["mahesh"])

#Add new pair in dictionary
my_dict["ramesh"] = 20
print(my_dict)

#Update existing dictionary
my_dict["mahesh"] = 250
print(my_dict)

#delete pair from dictionary
del my_dict["ramesh"]
print(my_dict)

#check length of dictionary
print(len(my_dict))