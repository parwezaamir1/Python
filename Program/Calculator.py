def add(x, y):
    return x+y


def subtract(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("""Select Operations
1.For Addition
2.For Subtraction
3.For Multiplication
4.For Division""")

while True:
    choices = int(input("Enter the choices 1/2/3/4 "))

    if choices == 1:
        print(add(x, y))
        break
    elif choices == 2:
        print(subtract(x, y))
        break
    elif choices == 3:
        print(multiplication(x, y))
        break
    elif choices == 4:
        print(division(x, y))
        break
    else:
        print("Invalid Input")
        continue

