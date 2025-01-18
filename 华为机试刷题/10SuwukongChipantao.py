
trees = list(map(int,input().split()))
trees.sort()
treeslen = len(trees)
hours = int(input())

if hours < treeslen:
    print(0)
elif hours == treeslen:
    print(max(trees))
else:
    i = 0 
    j = treeslen - 1
    while i <= j:
        cnt = 0
        mid = int((i+j)/2)
        K = trees[mid]
        
        for s in range(treeslen):
            if trees[s] <= K:
                cnt += 1
            else: 
                if trees[s] % K == 0:
                    cnt += int(trees[s]/K)
                else:
                    cnt = cnt + int(trees[s]/K) + 1
        if cnt > hours:
            i = int((i + j) / 2)
        elif cnt < hours:
            j = int((i + j) / 2)
        else:
            print(K)
            break