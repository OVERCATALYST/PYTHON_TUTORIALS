def replace_substring(s,old,new):
    return s.replace(old,new)

s=input("Enter the main string: ")
old=input("Enter the substring to replace: ")
new=input("Enter the new substring: ")

print("Modified string:",replace_substring(s,old,new))
