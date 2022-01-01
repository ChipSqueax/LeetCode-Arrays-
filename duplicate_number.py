nums = [1,3,4,2,2]
low = 0
high = len(nums) - 1
while low < high:
    mid = low + (high - low)//2
    count = 0
    for num in nums:
        if num <= mid:
            count += 1
    if count <= mid:
        low = mid + 1
    else:
        high = mid
print(low)