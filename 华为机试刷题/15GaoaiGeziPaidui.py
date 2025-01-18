
try:
    arr=list(map(int,input().split()))
    l = len(arr)
    for i in range(0,l - 2,2):
            # print(i)

        if arr[i] > arr[i+2] and arr[i+1] > arr[i+2]:
            tmp = arr[i+2]
            arr[i+2] = arr[i+1]
            arr[i+1] = tmp
        elif arr[i]<arr[i+1] and arr[i] < arr[i+1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
        # print(arr)
        # if arr[i] > arr[i+2] and arr[i+1] > arr[i+2]:
        #     tmp = arr[i+2]
        #     arr[i+2] = arr[i+1]
        #     arr[i+1] = tmp
    
    if arr[l -2] < arr[l - 1] and l % 2 == 0:
        tmp = arr[l -2]
        arr[l -2] = arr[l - 1]
        arr[l - 1] = tmp

    print(arr)

except ValueError:
    print("[]")