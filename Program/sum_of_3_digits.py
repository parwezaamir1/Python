# Input from user
num = int(input("Enter a three-digit number: "))

# Extracting digits
digit1 = num // 100
digit2 = (num % 100) // 10
digit3 = num % 10

# Calculating sum of digits
sum_of_digits = digit1 + digit2 + digit3

print(f"The sum of the digits in {num} is: {sum_of_digits}")
