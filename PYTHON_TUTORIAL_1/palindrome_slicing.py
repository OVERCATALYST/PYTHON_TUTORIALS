def is_palindrome(text):
    rev_text=text[::-1] 
    return text==rev_text

user_input = input("Enter a string to check if it is a palindrome: ")

if is_palindrome(user_input):
    print(f'"{user_input}" is a Palindrome.')
else:
    print(f'"{user_input}" is NOT a Palindrome.')