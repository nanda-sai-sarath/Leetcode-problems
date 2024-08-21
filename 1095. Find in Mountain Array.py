def findInMountainArray(nums, target):
    pivot = pivotElement(nums)
    start = 0
    end = len(nums) - 1

    if pivot == -1:
        return binarySearch(nums, target, start, end)
    
    if target == nums[pivot]:
        return pivot

    if target > nums[0]:
        return binarySearch(nums, target, start, pivot - 1)
    
    else:
        return binarySearch(nums, target, pivot + 1, end)

def pivotElement(nums):
    start = 0
    end = len(nums) - 1

    while(start < end):
        mid = (start + end) // 2
        if mid > end and nums[mid] > nums[mid + 1]:
            return mid
        if start < mid and nums[mid] < nums[mid - 1]:
            return mid - 1
        if nums[start] < nums[mid]:
            end = mid - 1
        else:
            start = mid - 1
    return -1
            

def binarySearch(nums, target, start, end):

    while start <= end:
        mid = start + (end - start) // 2

        if target == nums[mid]:
            return mid

        if target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
        
    return -1

nums = list(map(int,input().split()))
target = int(input())
print(findInMountainArray(nums, target))