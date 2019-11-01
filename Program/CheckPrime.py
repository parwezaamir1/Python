number = int(input("Enter the number to check "))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"Given number {number} is not a prime number")
            break
    else:
        print(f"{number} is prime number")
else:
    print(f"{number} is not prime number ")