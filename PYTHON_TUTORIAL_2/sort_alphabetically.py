n=int(input("Enter number of names: "))
names=[]
for i in range(n):
    name=input(f"Enter name {i+1}: ")
    names.append(name)
names.sort()
print("\nSorted Names:")
for name in names:
    print(name)