nterms = int(input("How many terms: "))
result = list(map(lambda x: 2 ** x, range(nterms)))

for i in range(nterms):
    print(f"2 raised to power {i} is {result[i]} ")
