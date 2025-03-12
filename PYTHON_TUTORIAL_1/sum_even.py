def calc(numbers):
    return sum(num for num in numbers if num % 2 == 0)  
numbers=[]
N=int(input("Enter the number of elements: "))
for i in range(N): 
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print(f"The sum of even numbers is: {calc(numbers)}")