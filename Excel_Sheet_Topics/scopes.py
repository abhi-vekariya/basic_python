# Global scope example

# Define a global variable
global_var = 100

def my_function():
    # Access global variable within the function
    print("Inside my_function - Global variable:", global_var)

# Call the function
my_function()  # Output: Inside my_function - Global variable: 100

# Access global variable outside the function
print("Outside my_function - Global variable:", global_var)  # Output: Outside my_function - Global variable: 100

# Local scope example

def my_function():
    # Define a local variable
    local_var = 200
    print("Inside my_function - Local variable:", local_var)

# Call the function
my_function()  # Output: Inside my_function - Local variable: 200
# Trying to access local variable outside the function will raise NameError
# print("Outside my_function - Local variable:", local_var)  # This will raise NameError

# Non-local scope example


def outer_function():
    outer_var = 300  # Define an outer (non-local) variable

    def inner_function():
        nonlocal outer_var  # Declare outer_var as non-local
        outer_var += 100  # Modify outer_var from the enclosing scope
        print("Inside inner_function - Modified outer_var:", outer_var)

    # Call the inner function
    inner_function()  # Output: Inside inner_function - Modified outer_var: 400

    # Print the value of outer_var after calling inner_function
    print("After inner_function - Outer_var:", outer_var)  # Output: After inner_function - Outer_var: 400

# Call the outer function
outer_function()



