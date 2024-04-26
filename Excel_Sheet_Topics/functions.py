import random
print("**************************square of number***********************************")
def square(number):
    """Function to calculate the square of a number."""
    result = number ** 2
    return result

# Calling the function
result = square(5)
print("Square of 5 is:", result)

print("********************************random color****************************************")
def color_selector(col1, col2):
    color = random.randint(0,1)
    if color == 0:
        return col1
    else:
        return col2

shirt_color = color_selector('pink','yellow')
print(shirt_color)


print("******************************factorial****************************")
# Define a recursive function to calculate factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Call the function to calculate factorial of a number
num = 5
result = factorial(num)
print(f"The factorial of {num} is: {result}")


print("******************************lambda****************************")
# Define a lambda function to calculate the square of a number
square = lambda x: x ** 2

# Call the lambda function
number = 4
result = square(number)
print(f"The square of {number} is: {result}")

print("*********************arbitrary arguments******************")
#*args is used to pass a variable number of positional arguments to a function.
def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_values(10, 20, 30, 40)
print("Sum:", result)  # Output: Sum: 100

print("*********************arbitrary keyword arguments****************")
#**kwargs is used to pass a variable number of keyword arguments to a function.
def display_info(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

display_info(name='xyz',age=50,school='abc')



