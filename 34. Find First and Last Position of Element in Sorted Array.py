def searchRange(nums, target):
    ans = [-1,-1]
    ans[0] = search(nums, target, True)
    ans[1] = search(nums, target, False)
    
    return ans
    
def search(nums, target, a):
    ans = -1
    start = 0
    end = len(nums) - 1

    while(start <= end):
        mid = (start + end) // 2
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            ans = mid
            if a:
                end = mid - 1
            else:
                start = mid + 1
            
    return ans
    
nums = list(map(int,input().split()))
target = int(input())
print(searchRange(nums, target))