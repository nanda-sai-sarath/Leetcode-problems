def twoSum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        y = target - num
        if y in d:
            return [d[y], i]
        d[num] = i

nums = list(map(int, input().split()))
target = int(input())
print(twoSum(nums, target))
