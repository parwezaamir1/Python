# num = int(input("Enter the number: "))
# temp = num
# rev = 0
# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10
# if num == rev:
#     print(f"{num} is palindrome number")
# else:
#     print(f"{num} is not palindrome number")

def palin(text):
    if len(text) <= 1:
        print("Palindrome")
    else:
        if text[0] == text[-1]:
            palin(text[1:-1])
        else:
            print("Not a palindrome")


palin("madam")
palin("python")
palin('121')