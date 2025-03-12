def find_median(numbers):
    numbers.sort()
    n=len(numbers)
    mid=n//2
    if n%2==0:
        return (numbers[mid-1]+numbers[mid])/2
    else:
        return numbers[mid]

n=int(input("Enter number of elements: "))
numbers=[float(input(f"Enter number {i+1}: ")) for i in range(n)]

print("Median:",find_median(numbers))