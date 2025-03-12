def check(a, b, c):
    s = sorted([a, b, c])
    return s[0]**2 + s[1]**2 == s[2]**2

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if check(a, b, c):
    print("Right-angled triangle.")
else:
    print("NOT a right-angled triangle.")
