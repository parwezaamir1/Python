num = int(input("Enter the number: "))
order = len(str(num))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** order
    temp //= 10
if num == sum:
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")
