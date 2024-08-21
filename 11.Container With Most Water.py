def maxArea(height):

    l = 0
    r = len(height) - 1
    ans = 0

    while l < r:
        width = r - l
        minHeight = min(height[l], height[r])
        area = minHeight * width
        ans = max(ans, area)
        print(width, minHeight, area, ans)

        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            l += 1
            r -= 1

    return ans


height = list(map(int,input().split()))
print(maxArea(height))