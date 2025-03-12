import math
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def sin_series(x,n_terms):
    x=math.radians(x)
    sin_value=0
    for n in range(n_terms):
        term=((-1)**n*x**(2*n+1))/factorial(2*n+1)
        sin_value+=term
    return sin_value
x=float(input("Enter angle in degrees: "))
n_terms=int(input("Enter number of terms: "))
result=sin_series(x,n_terms)
print(f"sin({x}) ≈ {result}")
