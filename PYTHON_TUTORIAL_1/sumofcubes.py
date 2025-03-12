def calc(n):
    return sum(i**3 for i in range(2, n+1, 2))
n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print(f"The sum of cubes of all even numbers up to {n} is: {calc(n)}")