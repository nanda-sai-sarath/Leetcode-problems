def MissingNumber(arr):
    i=0
    while(i < len(arr)):
        correct = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[correct]:
            arr[i],arr[correct]=arr[correct],arr[i]
        else:
            i+=1
    
    for i in range(len(arr)):
        if arr[i] != i:
            return i
            
    return len(arr)
    
arr=list(map(int,input().split()))
print(MissingNumber(arr))