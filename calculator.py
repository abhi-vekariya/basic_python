print("please choose number: \n \
    1. add\n \
    2. subtract\n \
    3. multiply\n \
    4. division\n")
num = int(input("Enter your number: "))
a = int(input("first number: "))
b = int(input("second number: "))

def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def division(a,b):
    print(a/b)

if (num == 1):
    add(a,b)
elif (num == 2):
    subtract(a,b)
elif (num == 3):
    multiply(a,b)
elif (num == 4):
    division(a,b)
else:
    print("Given number is not acceptable")