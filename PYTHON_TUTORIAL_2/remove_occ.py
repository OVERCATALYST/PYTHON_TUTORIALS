def remove_substring(s,sub):
    return s.replace(sub,"")
s=input("Enter the main string: ")
sub=input("Enter the substring to remove: ")
print("String after removal:",remove_substring(s,sub))