def findErrorNums(nums):
    ans,i=[],0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i],nums[correct]=nums[correct],nums[i]
        else:
            i+=1
    print(nums)
    for i in range(len(nums)):
        if i+1 != nums[i]:
            ans.append(nums[i])
            ans.append(i+1)
    return ans

nums=list(map(int,input().split()))
print(findErrorNums(nums))
