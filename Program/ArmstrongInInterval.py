n1 = int(input("Enter the lower number: "))
n2 = int(input("Enter the upper number: "))
for num in range(n1, n2+1):
    order = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** order
        temp //=10
    if num == sum:
        print(num)
