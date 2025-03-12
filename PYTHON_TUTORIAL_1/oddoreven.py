def check(number):
    if number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

num=int(input("Enter the number:"))
check(num)