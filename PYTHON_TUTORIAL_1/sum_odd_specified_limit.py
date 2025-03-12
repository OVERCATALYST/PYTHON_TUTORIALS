def sum_of_odd(lower,upper):
    total=0
    for num in range(lower,upper+1):
        if num%2!=0:
            total+=num
    return total

lower=int(input("Enter lower limit: "))
upper=int(input("Enter upper limit: "))

print(f"Sum of odd numbers={sum_of_odd(lower,upper)}")
