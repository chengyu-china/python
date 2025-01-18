from itertools import combinations


cpus = []

str1 = input()

for e in str1:
    if e.isdigit():
        cpus.append(int(e))
cpus.sort()
num = int(input())

arr1cpus = []
arr2cpus = []
result = []

for i in range(len(cpus)):
    if cpus[i] >= 4:
        arr2cpus.append(cpus[i])
    else:
        arr1cpus.append(cpus[i])

if num == 8:
    if len(cpus) == 8:
        result.append(cpus)
elif num == 4:
    if len(arr2cpus) == 4:
        result.append(arr2cpus)
    if len(arr1cpus) == 4:
        result.append(arr1cpus)
elif num ==2:
    if len(arr1cpus) % 2 == 0 and len(arr2cpus) % 2 == 1:
        if len(arr1cpus) == 0:
            for cmb in combinations(arr2cpus,2):
                result.append(list(cmb))
        else:
            for cmb in combinations(arr1cpus,2):
                result.append(list(cmb))
    elif len(arr1cpus) % 2 == 1 and len(arr2cpus) % 2 == 0:
        if len(arr2cpus) == 0:
            for cmb in combinations(arr1cpus,2):
                result.append(list(cmb))        
        else:
            for cmb in combinations(arr2cpus,2):
                result.append(list(cmb))
    elif len(arr1cpus) % 2 == 1 and len(arr2cpus) % 2 == 1:
        for cmb in combinations(arr1cpus,2):
            result.append(list(cmb))
        for cmb in combinations(arr2cpus,2):
            result.append(list(cmb))
    else:
        if len(arr1cpus) > 0 and len(arr2cpus) >0:
            if len(arr1cpus) > len(arr2cpus):
                for cmb in combinations(arr2cpus,2):
                    result.append(list(cmb))
            elif len(arr1cpus) < len(arr2cpus): 
                for cmb in combinations(arr1cpus,2):
                    result.append(list(cmb))
            else:
                for cmb in combinations(arr1cpus,2):
                    result.append(list(cmb))
                for cmb in combinations(arr2cpus,2):
                    result.append(list(cmb))
        elif len(arr1cpus) == 0 and len(arr2cpus) >0:
            for cmb in combinations(arr2cpus,2):
                result.append(list(cmb))
        else:
            for cmb in combinations(arr1cpus,2):
                result.append(list(cmb))
else:
    if len(arr1cpus) % 2 == 0 and len(arr2cpus) % 2 == 1:
        for cmb in combinations(arr2cpus,1):
            result.append(list(cmb))

    elif len(arr1cpus) % 2 == 1 and len(arr2cpus) % 2 == 0:
        for cmb in combinations(arr1cpus,1):
            result.append(list(cmb))
    
    elif len(arr1cpus) % 2 == 1 and len(arr2cpus) % 2 == 1:
        if len(arr1cpus) > len(arr2cpus):
            for cmb in combinations(arr2cpus,1):
                result.append(list(cmb))
        elif len(arr1cpus) < len(arr2cpus): 
            for cmb in combinations(arr1cpus,1):
                result.append(list(cmb))
        else:
            for cmb in combinations(arr1cpus,1):
                result.append(list(cmb))
            for cmb in combinations(arr2cpus,1):
                result.append(list(cmb))
    else:
        if len(arr1cpus) > 0 and len(arr2cpus) >0:
            if len(arr1cpus) > len(arr2cpus):
                for cmb in combinations(arr2cpus,1):
                    result.append(list(cmb))
            elif len(arr1cpus) < len(arr2cpus): 
                for cmb in combinations(arr1cpus,1):
                    result.append(list(cmb))
            else:
                for cmb in combinations(arr1cpus,1):
                    result.append(list(cmb))
                for cmb in combinations(arr2cpus,1):
                    result.append(list(cmb))
        elif len(arr1cpus) == 0 and len(arr2cpus) >0:
            for cmb in combinations(arr2cpus,1):
                result.append(list(cmb))
        else:
            for cmb in combinations(arr1cpus,1):
                result.append(list(cmb))

print(result)