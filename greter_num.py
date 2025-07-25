# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))
number5 = int(input("Enter the fifth number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
largest_number = number1

if number2 > largest_number:
    largest_number = number2
if number3 > largest_number:
    largest_number = number3
if number4 > largest_number:
    largest_number = number4
if number5 > largest_number:
    largest_number = number5

print("The largest number is:", largest_number)
