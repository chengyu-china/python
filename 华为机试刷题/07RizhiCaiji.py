
arr  = list(map(int,input().split()))
arrlen = len(arr)
score = [0]*arrlen

if arrlen == 1:
    print(arr[0])
    exit()


for i in range(arrlen):
    if sum(arr[0:i+1]) <= 100:
        tmp = sum(arr[0:i+1])
    else:
        tmp = 100 - (sum(arr[0:i+1]) - 100)
    
    sub = 0

    for j in range(i+1):
        sub += arr[j] * (i-j)

    score[i] = tmp - sub

print(max(score))