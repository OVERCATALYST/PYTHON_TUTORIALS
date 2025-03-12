"""The quadratic formula is 
x=(-b+-root(b^2-4ac))/2a"""

from math import sqrt
def calc(a,b,c):
    disc=b**2-4*a*c

    if disc<0:
        rp=-b/(2*a)
        ip=sqrt(abs(disc))/(2*a)
        print(f"The complex roots: {rp:.2f} +- {ip:.2f}i")
    elif disc>0:
        r1=(-b+sqrt(disc)/(2*a))
        r2=(-b-sqrt(disc)/(2*a))
        print(f"Two real roots(distinct): {r1:.2f} and {r2:.2f}")
    else:
        root=-b/(2*a)
        print(f"One root(real):{root:.2f}")

a=float(input("Enter the coefficient a: "))
b=float(input("Enter the coefficient b: "))
c=float(input("Enter the coefficient c: "))

if a==0:
    print("a cannot be zero. Cannot accept")
else:
    calc(a,b,c)