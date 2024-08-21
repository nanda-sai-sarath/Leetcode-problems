def findDuplicates(nums):
    seen=set(nums)
    ans=[]
    # while(i < len(nums)):
    #     correct = nums[i]-1
    #     if nums[i] != nums[correct]:
    #         nums[i],nums[correct]=nums[correct],nums[i]
    #     else:
    #         i+=1
    # print(nums)
    # for i in range(len(nums)):
    #     if nums[i] != i+1:
    #         ans.append(nums[i])

    # return ans
    for i in range(1,len(nums)+1):
        if i not in seen:
            ans.append(nums[i])
    return ans



nums=list(map(int,input().split()))
print(findDuplicates(nums))