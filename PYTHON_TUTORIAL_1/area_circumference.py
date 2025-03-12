from math import pi

def calc(rad):
    area=pi*rad**2
    circumference=2*pi*rad
    return area,circumference

radius=float(input("Enter the radius of the circle:"))
area,circumference=calc(radius)

print(f"Area of circle with radius {radius} is: {area:.2f}")
print(f"Circumference of circle with radius {radius} is: {circumference:.2f}")