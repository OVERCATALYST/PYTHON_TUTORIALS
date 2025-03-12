def sum_of_digits(n):
    total=0
    while n>0:
        total+=n%10
        n//=10
    return total

print("Numbers between 100 and 1000 whose sum of digits is divisible by 9:")

for num in range(100,1000):
    if sum_of_digits(num)%9==0:
        print(num,end=" ")