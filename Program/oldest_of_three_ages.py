# User will input (3ages).Find the oldest one

def greatest_of_three_ages(a1, a2, a3):
    if a1 > a2 and a1 > a3:
        print("first person age", a1, "is the greatest")
    elif a2 > a1 and a2 > a3:
        print("Second person age", a2, "is the greatest")
    else:
        print("Third person age", a3, "is the greatest")

age1 = int(input("Enter the first age of a person: "))
age2 =  int(input("Enter the second age of a person: "))
age3 =  int(input("Enter the third age of a person: "))
greatest_of_three_ages(age1, age2, age3)
