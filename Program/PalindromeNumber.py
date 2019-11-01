num = int(input("Enter the number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if num == rev:
    print(f"{num} is palindrome number")
else:
    print(f"{num} is not palindrome number")