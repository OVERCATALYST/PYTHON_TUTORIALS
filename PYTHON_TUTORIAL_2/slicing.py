def split_string(s):
    even_chars=""
    odd_chars=""
    for i in range(len(s)):
        if i%2==0:
            even_chars+=s[i]
        else:
            odd_chars+=s[i]
    return even_chars,odd_chars
s=input("Enter a string: ")
even_part,odd_part=split_string(s)
print("Characters at even indices:",even_part)
print("Characters at odd indices:",odd_part)
