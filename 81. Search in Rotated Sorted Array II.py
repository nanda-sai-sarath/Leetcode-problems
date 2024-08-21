class Solution:
    def search(self, nums, target):
        if not nums:
            return False

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return True

            if nums[start] == nums[mid] == nums[end]:
                start += 1
                end -= 1

            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False

nums = list(map(int,input().split()))
target = int(input())
solution = Solution()
print(solution.search(nums, target))