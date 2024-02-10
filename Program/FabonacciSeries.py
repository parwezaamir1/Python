# nterms = int(input("How many terms "))
# n1 = 0
# n2 = 1
# count = 0
# if nterms <= 0:
#     print("Sorry, Please enter positive number")
# elif nterms == 1:
#     print(f"Fabonacci sequence upto {nterms}: ")
#     print(n1)
# else:
#     print(f"fabonacci sequence upto {nterms}: ")
#     while count < nterms:
#         print(n1, end=',')
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count = count + 1


# 0, 1, 1, 2, 3, 5, 8.....................

# def fib(m):
#     if m == 0 or m == 1:
#         return 1
#     else:
#         return fib(m-1) + fib(m-2)

# print(fib(48))



def fib(m, d):
    if m in d:
        return d[m]
    else:
        d[m] = fib(m-1, d) + fib(m-2, d)
        return d[m]

d = {1: 0, 2: 1}
m = int(input("Enter the number till you want to print fibonacci: "))
fibonacci_series = []
for i in range(1, m+1):
    fibonacci_series.append(fib(i, d))

print("Fibonacci series till the 14th term:", fibonacci_series)