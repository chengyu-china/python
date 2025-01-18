
# money = int(input())
# cnt = 0 
# i = 1
# while i <= money:
#     w = str(i)
#     if '4' in w:
#         cnt += 1
#     i += 1

# print(money - cnt)



# import sys
 
# for line in sys.stdin:
#     N = line.strip()
#     index =0
 
#     offset = 0
#     before_offset = 0
#     while index<len(N):
#         cur_n = N[len(N)-1-index]
#         if cur_n!="0":
#             offset += int(cur_n)*before_offset
#             if cur_n>"4":
#                 offset += 10**index-before_offset
#         before_offset = before_offset*9+ 10**index
#         index += 1
#     print(int(N)-offset)


money = input()

new_money = []

for i in range(len(money)):
    if int(money[i])>=5:
       new_money.append(int(money[i]) - 1)
    else: 
        new_money.append(int(money[i]))

# print(new_money)

res = 0

for i in range(len(new_money)):
    res += new_money[i]*9**(len(new_money)-i -1)


print(res)

 

