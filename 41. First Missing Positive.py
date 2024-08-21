def firstMissingPositive(nums):
    seen=set(nums)
    for i in range(1,len(nums)):
        if i not in seen:
            ans=i
            break
    return ans

nums=list(map(int,input().split()))
print(firstMissingPositive(nums))