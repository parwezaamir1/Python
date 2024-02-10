
def is_even(number):
    if number % 2 == 0:
            return "Even"
    else:
            return "Odd"
    

number = int(input("Enter the number to check even or odd: "))
print(is_even(number))