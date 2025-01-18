
data = list(map(int,input().split()))

n = data[0]
m = data[1]
subjects = input().split()
students = []
tuplelen = 0

for i in range(n):
    infor = input().split()
    l = len(infor)
    sumscore = sum(map(int,infor[1:l]))
    infor.append(sumscore)
    students.append(tuple(infor))
order = input()

print(students)

if order not in subjects:
    # sorted(students,key=lambda x: x[-1])
    print(' '.join(map(lambda x:x[0],sorted(students,key=lambda x: (-x[-1],x[0])))))
else:
    for i in range(m):
        if order == subjects[i]:
            print(' '.join(map(lambda x:x[0],sorted(students,key=lambda x: (-x[i + 1],x[0])))))
