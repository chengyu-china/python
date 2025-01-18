import sys

str1 = input()
d = {}
for e in str1:
    d[e] = str1.count(e)

# print(d.keys())

print(''.join(map(lambda x: x[0],sorted(d.items(),key= lambda x : (-x[1], x[0])))))
