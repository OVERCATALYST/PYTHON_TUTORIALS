def check(n):
    if n < 2:
        return False 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 
num = int(input("Enter a number: "))

if check(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is NOT a Prime number.")
