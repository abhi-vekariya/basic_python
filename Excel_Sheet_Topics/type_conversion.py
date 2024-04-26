# Integer to Float
x = 10
float_value = float(x)
print("Integer to Float:")
print("Original Integer:", x)
print("Converted Float:", float_value)
print()

# Float to Integer
y = 3.14
int_value = int(y)
print("Float to Integer:")
print("Original Float:", y)
print("Converted Integer:", int_value)
print()

# Integer to String
num = 100
str_value = str(num)
print("Integer to String:")
print("Original Integer:", num)
print("Converted String:", str_value)
print()

# String to Integer
number_str = "50"
int_value_str = int(number_str)
print("String to Integer:")
print("Original String:", number_str)
print("Converted Integer:", int_value_str)
print()

# String to Float
pi_str = "3.14"
float_value_str = float(pi_str)
print("String to Float:")
print("Original String:", pi_str)
print("Converted Float:", float_value_str)
print()

# Handling ValueError during conversion
invalid_str = "hello"
try:
    converted_value = int(invalid_str)
    print("Converted Integer (from invalid string):", converted_value)
except ValueError as e:
    print("ValueError occurred during conversion:", e)
