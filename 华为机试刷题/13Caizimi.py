
wlist = list(map(lambda x :''.join(sorted(set(x))) ,input().split(',')))

alist = input().split(',')

output = []

for e in wlist:
    for t in alist:
        q = ''.join(sorted(set(t)))
        if e == q:
            output.append(t)

if len(output) == 0:
    print('not found')
else:
    print(','.join(output))


