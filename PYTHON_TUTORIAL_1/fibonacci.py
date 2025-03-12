def fibonacci():
    FS=[]
    a=0  
    b=1  
    FS.append(a)
    FS.append(b)
    for i in range(8):
        next_number = a + b 
        FS.append(next_number) 
        a=b
        b = next_number
    return FS
fibonacci_series=fibonacci()
print("The first 10 Fibonacci numbers are:", fibonacci_series)
