def remove_duplicates(lst):
    return list(set(lst))

n=int(input("Enter number of elements: "))
numbers=[int(input(f"Enter number {i+1}: ")) for i in range(n)]

print("List without duplicates:",remove_duplicates(numbers))
