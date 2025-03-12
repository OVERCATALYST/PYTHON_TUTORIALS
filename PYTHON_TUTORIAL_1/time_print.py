sec=int(input("Enter time in seconds"))
hr=sec//3600
ms=(sec%3600)//60
ss=sec%60
print("Time in HH:MM:SS:",f"{hr:02d}:{ms:02d}:{ss:02d}")