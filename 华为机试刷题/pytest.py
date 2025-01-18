list1 = [1,2,3]
list2 = [2,3,4]
list3 = []

for i in range(len(list1)): 
    if list1[i] in list2:
        list3.append(list1[i])

print(list3)