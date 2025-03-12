def decimal_to_binary(n):
    binary_str=""
    if n==0:
        return "0"
    while n>0:
        remainder=n%2
        binary_str=str(remainder)+binary_str
        n//=2
    return binary_str
n=int(input("Enter a decimal number: "))
binary_result=decimal_to_binary(n)
print(f"Binary equivalent of {n} is: {binary_result}")