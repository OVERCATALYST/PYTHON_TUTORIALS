def separate_types(lst):
    integers=[]
    floats=[]
    strings=[]
    
    for item in lst:
        if isinstance(item,int):
            integers.append(item)
        elif isinstance(item,float):
            floats.append(item)
        else:
            strings.append(item)
    
    return integers,floats,strings

n=int(input("Enter number of elements: "))
mixed_list=[]

for i in range(n):
    value=input(f"Enter element {i+1}: ")
    try:
        if "." in value:
            mixed_list.append(float(value))
        else:
            mixed_list.append(int(value))
    except ValueError:
        mixed_list.append(value)

ints,floats,strs=separate_types(mixed_list)

print("Integers:",ints)
print("Floats:",floats)
print("Strings:",strs)
