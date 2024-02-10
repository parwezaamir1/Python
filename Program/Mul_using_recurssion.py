def mul(a, b):

    if b == 1:
        return a
    else:
        return a + mul(a, b-1)
    

# 3 * 4
    #  3 + 3*3
    #  3 + 3 + 3 * 2............  use pythontutor for more visualization

print(mul(3,4))