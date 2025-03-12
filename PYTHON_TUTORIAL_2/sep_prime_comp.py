def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def separate_numbers(lst):
    primes=[num for num in lst if is_prime(num)]
    composites=[num for num in lst if not is_prime(num) and num>1]
    return primes,composites

n=int(input("Enter number of elements: "))
numbers=[int(input(f"Enter number {i+1}: ")) for i in range(n)]

primes,composites=separate_numbers(numbers)

print("Prime numbers:",primes)
print("Composite numbers:",composites)