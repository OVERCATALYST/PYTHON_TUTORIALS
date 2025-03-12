def calc(numbers):
    sp = sn = cp = cn=0
    for num in numbers:
        if num > 0:
            sp += num
            cp += 1
        elif num < 0:
            sn += num
            cn += 1
    avg_pos = sp / cp if cp > 0 else 0
    avg_neg = sn / cn if cn > 0 else 0
    return sp, avg_pos, sn, avg_neg
numbers = []
for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
sum_pos, avg_pos, sum_neg, avg_neg = calc(numbers)
print("Sum of positive numbers:", sum_pos)
print("Average of positive numbers:", round(avg_pos, 2))
print("Sum of negative numbers:", sum_neg)
print("Average of negative numbers:", round(avg_neg, 2))