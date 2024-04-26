# Simple if-else statement example
num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive")
else:
    print("Number is either zero or negative")


# if-elif-else statement example
num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")

# Nested if statement example
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")

