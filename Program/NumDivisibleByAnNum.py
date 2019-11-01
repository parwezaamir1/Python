my_list = [10, 15, 12, 14, 75, 45, 84, 58, 56, 85, 45, 95, 100, 214, 215]
result = list(filter(lambda x: (x % 5 == 0), my_list))

print(result)
