def check(num1,num2):
    if num1>num2:
        print(f"{num1} is greater than {num2}")
    elif num1<num2:
        print(f"{num1} is less than {num2}")
    else:
        print(f"{num1} is equal to {num2}")

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
check(a,b)