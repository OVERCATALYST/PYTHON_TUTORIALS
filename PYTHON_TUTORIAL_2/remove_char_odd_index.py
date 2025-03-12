def remove_odd_indices(s):
    result=""
    for i in range(len(s)): 
        if i%2==0:  
            result+=s[i] 
    return result  
s=input("Enter a string: ")
print(f"String after removing odd index characters: {remove_odd_indices(s)}")