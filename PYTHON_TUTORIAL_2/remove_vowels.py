def remove_vowels(s):
    result="" 
    for c in s: 
        if c.lower() not in "aeiou": 
            result+=c
    return result 
s=input("Enter a string: ")
print(f"String without vowels: {remove_vowels(s)}")
