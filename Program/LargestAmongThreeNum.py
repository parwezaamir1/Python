a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter thr third number "))

if (a > b) and (a > c):
    print(f"{a} is largest among {a}, {b} and {c}")
elif (b > a) and (b > c):
    print(f"{b} is largest among {a}, {b} and {c}")
else:
    print(f"{c} is largest among {a}, {b} and {c}")
