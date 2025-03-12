def reverse_number(n):
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    n_str = str(n)  
    reversed_str = "" 
    for i in range(len(n_str) - 1, -1, -1):
        reversed_str += n_str[i] 
    reversed_number = int(reversed_str)

    if is_negative:
        reversed_number = -reversed_number
    return reversed_number

num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print("Reversed number:", reversed_num)