def is_armstrong(number):
    org=number
    num_digits=len(str(number))  
    sop=0 
    while number>0:
        digit=number%10 
        sop+=digit**num_digits  
        number//=10  
    return sop==org

num=int(input("Enter a number to check if it is an Armstrong number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")