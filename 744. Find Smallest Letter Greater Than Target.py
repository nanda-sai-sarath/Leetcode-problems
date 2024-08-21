def nextGreatestLetter(letters, target):
    start = 0
    end = len(letters) - 1
    if target >= letters[end]:
        return letters[start]
    while start <= end:
        mid = (start + end) // 2
        if target < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    return letters[start]
    
letters = list(map(str,input().split()))
target = input()
print(nextGreatestLetter(letters, target))