str1 = input()
n = int(input())

ch_cnt = {}

for e in str1:
    ch_cnt[e]=0

cnt = 1
for i in range(1,len(str1)+1):
    if i < len(str1) and str1[i-1] == str1[i]:
        cnt += 1
    else:
        ch_cnt[str1[i-1]] = max(ch_cnt[str1[i-1]],cnt)
        cnt = 1

arr = list(ch_cnt.values())

arr.sort(reverse=True)

if n <= 0  or n > len(arr):
    print(-1)
else:
    print(arr[n-1])


# AAAAHHHBBCDHHHH