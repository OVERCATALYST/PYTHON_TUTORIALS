def calc(n):
    i=2
    while i*i<=n:
        while n%i==0:
            print(i,end=" ")
            n//=i
        i+=1
    if n>1:
        print(n)
num=int(input("Enter a number: "))
print("Prime factors:",end=" ")
calc(num)