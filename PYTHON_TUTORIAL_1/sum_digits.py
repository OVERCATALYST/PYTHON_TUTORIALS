def calc(n):
    return sum(int(digit) for digit in str(abs(n)))  

num = int(input("Enter a number: "))

print(f"The sum of the digits of {num} is {calc(num)}.")
