def check_even_odd(n):
    return "Even" if n%2==0 else "Odd"
def check_number_sign(n):
    if n>0:
        return "Positive"
    elif n<0:
        return "Negative"
    else:
        return "Zero"
def generate_factors(n):
    return [i for i in range(1,n+1) if n%i==0]
while True:
    print("\nMenu:")
    print("1. Check Even or Odd")
    print("2. Check Positive, Negative, or Zero")
    print("3. Generate Factors of a Number")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        num=int(input("Enter a number: "))
        print("Result:",check_even_odd(num))
    elif choice==2:
        num=int(input("Enter a number: "))
        print("Result:",check_number_sign(num))
    elif choice==3:
        num=int(input("Enter a number: "))
        print("Factors:",generate_factors(num))
    elif choice==4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")
