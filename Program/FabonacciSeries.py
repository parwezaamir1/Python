nterms = int(input("How many terms "))
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
    print("Sorry, Please enter positive number")
elif nterms == 1:
    print(f"Fabonacci sequence upto {nterms}: ")
    print(n1)
else:
    print(f"fabonacci sequence upto {nterms}: ")
    while count < nterms:
        print(n1, end=',')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1
