from math import sqrt
def distance(x1,y1,x2,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)

x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))

print(f"Distance={distance(x1,y1,x2,y2):.2f}")
