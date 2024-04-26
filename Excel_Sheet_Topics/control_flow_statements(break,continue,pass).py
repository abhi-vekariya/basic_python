# Example of using break statement in a loop
print("*********************break***************************")
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 30:
        print("Found the number 30!")
        break  # Exit the loop when num is 30

    print(num)  # Print each number as we iterate through the list

print("Loop ended")

print("******************continue*************************")
# Example of using continue statement in a loop
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers

    print(f"Processing number: {num}")

print("Loop ended")

print("*****************pass***************************")
# Example of using pass statement
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        pass  # Placeholder (no action needed for num == 3)
    else:
        print(f"Processing number: {num}")

print("Loop ended")


