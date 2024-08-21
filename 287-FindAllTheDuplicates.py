def findDuplicate(nums):
    i=0
    while(i < len(nums)):
        correct = nums[i]
        if nums[i] < len(nums) and nums[i] != nums[correct]:
            nums[i],nums[correct]=nums[correct],nums[i]
        else:
            i+=1
    return nums[0]
nums=list(map(int,input().split()))
print(findDuplicate(nums))