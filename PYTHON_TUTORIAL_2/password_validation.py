def check(password):
    if len(password)<6:
        return False
    hl=hu=hd=hs=False
    for i in password:
        if 'a'<=i<='z':
            hl=True
        elif 'A'<=i<='Z':
            hu=True
        elif '0'<=i<='9':
            hd=True
        elif i in "$#@":
            hs=True
    return hl and hu and hd and hs
password=input("Enter a password: ")
if check(password):
    print("Valid password")
else:
    print("Invalid password")
