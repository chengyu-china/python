import sys

str1 = input().split()
a = int(str1[0])
b = int(str1[1])

def biggestyinshu(a,b):
    if a < b:
        s = a 
        a = b 
        b = s
    while True:
        if a % b == 0:
            break
        else:
            m = a % b
            a = b 
            b = m 
    return b 

m = biggestyinshu(a,b)

print(int(a*b/m))