def modify_string(s):
    return s.replace(" ","*") if " " in s else f"${s}$"

s=input("Enter a string: ")
print(f"Modified string: {modify_string(s)}")