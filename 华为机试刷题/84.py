arr = [int(e) for e in input().split(',')]
result = int(input())

i, j = 0,1

current_sum = 0 
maxlen = 1

for i in range(len(arr)):
    for j in range(j,len(arr)):
        if arr[j] > arr[i]:
            current_sum = current_sum + arr[i]
            j += 1
            maxlen += 1
        else:
            i = j
            j += 1
