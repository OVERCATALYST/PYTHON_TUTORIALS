def calc(n):
    result=(2**(2*n))+n+5 
    return result

n = int(input("Enter the value of n: "))
value=calc(n)
print(f"The value of 2^(2*{n})+{n}+5 is: {value}")