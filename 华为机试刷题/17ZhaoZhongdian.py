arr = list(map(int,input().split()))
arrlen = len(arr)
mid = int(arrlen / 2)

steps = []

for i in range(mid):
    step = 2
    j = i + arr[i]
    while True:
        if j == arrlen - 1:
            # print(step)
            steps.append(step)
            break
        elif j >= arrlen:
            # steps.append(-1)
            # print(-1)
            break
        else:
            j = j + arr[j]
            step += 1
if len(steps) == 0:
    print(-1)
else:
    steps.sort()
    print(steps[0])