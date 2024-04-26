#For Loop Example :
# List of numbers
print("***************************Use of For Loop*********************************")
numbers = [10, 5, -3, 8, 0, 12]

# Initialize variables to keep track of results
sum_positive = 0
count_negative = 0
sum_even = 0
product_odd = 1

# Iterate over the list of numbers using a for loop
for num in numbers:
    # Check if the number is positive
    if num > 0:
        sum_positive += num  # Add positive number to sum

    # Check if the number is negative
    elif num < 0:
        count_negative += 1  # Increment negative numbers count

    # Check if the number is even
    if num % 2 == 0:
        sum_even += num  # Add even number to sum

    # Check if the number is odd
    elif num % 2 != 0:
        product_odd *= num  # Multiply odd number to product

# Output the results after processing the list
print("Sum of positive numbers:", sum_positive)
print("Count of negative numbers:", count_negative)
print("Sum of even numbers:", sum_even)
print("Product of odd numbers:", product_odd)

#---------------------------------------------------------------------------------------------

#While Loop example
# Countdown timer using a while loop
print("****************************Use of While loop***************************************")
countdown_start = 5  # Initial countdown value

print("Starting countdown...")

while countdown_start > 0:
    print(countdown_start)
    countdown_start -= 1  # Decrement the countdown value

print("GO!")


#Pattern Code with While
#****
#***
#**
#*
i = 4

while i > 0:

    j = 1
    while j <= i:
        print("*",end= ' ')
        j += 1

    print()
    i -= 1


