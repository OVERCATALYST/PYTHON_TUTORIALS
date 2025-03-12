def mult(n):
    for num in range(1,n+1): 
        print(f"\nMultiplication Table of {num}") 
        print("-"*25)
        for m in range(1,11): 
            result=num*m 
            print(f"{num}x{m}={result}")  
n = int(input("Enter the value of n: "))
mult(n)
