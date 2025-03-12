def bubble_sort(lst):
    n=len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

n=int(input("Enter number of elements: "))
numbers=[int(input(f"Enter number {i+1}: ")) for i in range(n)]

sorted_numbers=bubble_sort(numbers)

print("Sorted list:",sorted_numbers)
