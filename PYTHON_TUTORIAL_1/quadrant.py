def check(x, y):
    if x > 0 and y > 0:
        return "1st Quadrant"
    elif x < 0 and y > 0:
        return "2nd Quadrant"
    elif x < 0 and y < 0:
        return "3rd Quadrant"
    elif x > 0 and y < 0:
        return "4th Quadrant"
    elif x == 0 and y != 0:
        return "On the Y-axis"
    elif y == 0 and x != 0:
        return "On the X-axis"
    else:
        return "At the Origin"

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

print(f"The point ({x}, {y}) lies in the {check(x, y)}.")
