# Initialize an empty list
numbers = []

# Get the number of values to input
n = int(input("Enter the number of values: "))

# Input n values and append to the list
for i in range(n):
    num = input(f"Enter value {i+1}: ")
    numbers.append(num)

# Display each element and its maximum digit
for num in numbers:
    max_digit = '0'
    for digit in num:
        if digit > max_digit:
            max_digit = digit
    print(f"Number: {num}, Maximum Digit: {max_digit}")
