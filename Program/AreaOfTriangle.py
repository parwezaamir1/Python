a = input("Enter the value of first sides of triangle  ")
b = input("Enter the value of second sides of triangle ")
c = input("Enter the value of third sides of triangle  ")

s = ((float(a))+(float(b))+(float(c))) / 2
area = (s*(s-float(a))*(s-float(b))*(s-float(c))) **0.5
print(f"The area of the triangle is {area} ")