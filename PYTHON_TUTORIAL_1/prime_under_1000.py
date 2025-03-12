def is_prime(number):
    if number<2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i==0:  
            return False
    return True  

def primes_below_1000():
    prime_num= [] 
    for num in range(2,1000): 
        if is_prime(num):
            prime_num.append(num)

    print("Prime numbers less than 1000:")
    for prime in prime_num:
        print(prime,end=" ") 
primes_below_1000()
