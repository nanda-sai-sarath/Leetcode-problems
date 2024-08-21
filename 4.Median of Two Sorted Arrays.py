def findMedian(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    if len(nums1) % 2 != 0:
        return float(nums1[len(nums1) // 2])
    else:
        return (nums1[len(nums1) // 2] + nums1[(len(nums1) // 2) - 1]) / 2

nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(findMedian(nums1,nums2))