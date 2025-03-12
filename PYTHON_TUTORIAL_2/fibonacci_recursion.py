def fibonacci(n):
    if n<=0:
        return "Invalid input! Enter a positive integer."
    elif n==1:
        return 0
    elif n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the position of Fibonacci number: "))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
