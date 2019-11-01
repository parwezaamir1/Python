def print_factor(num):
    print(f"The factor of {num} are: ")
    for i in range(1, num+1):
        if num % i == 0:
            print(i)


num = int(input("Enter the number: "))
print(print_factor(num))


