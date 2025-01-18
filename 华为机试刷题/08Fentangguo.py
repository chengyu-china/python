

num = int(input())
cnt = 0

while num > 1:
    if num % 2 == 0:
        num = num / 2
    else:
        if (num == 3) or (num & 2 ) == 0:
            num -= 1
        else:
            num += 1
    
    cnt += 1

print(cnt)