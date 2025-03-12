from collections import Counter
def find_mode(numbers):
    freq=Counter(numbers)
    max_count=max(freq.values())
    mode=[num for num,count in freq.items() if count==max_count]
    return mode

n=int(input("Enter number of elements: "))
numbers=[int(input(f"Enter number {i+1}: ")) for i in range(n)]

mode=find_mode(numbers)
print("Mode:",mode if len(mode)>1 else mode[0])