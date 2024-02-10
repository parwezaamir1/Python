# num = int(input("Enter the number: "))
# factorial = 1
# if num < 0:
#     print("Sorry, Factorial of negative number is not exist")
# elif num == 0:
#     print(f"factorial of {num} is 1")
# else:
#     for n in range(1, num+1):
#         factorial = factorial * n
# print(f"Factorial of {num} is: {factorial}")


def fact(number):
    if number >= 0:
        if number == 0 or number == 1:
            return 1
        else:
            return number * fact(number-1)
    else:
        return "Invalid number, enter positive or zero number"
    
print(fact(0))
