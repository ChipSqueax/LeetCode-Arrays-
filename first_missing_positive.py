# Solution 1
nums = [1, 2, 3, 4, 5, 6]
nums.append(0)
for i in range(len(nums)):
    if nums[i] < 0 or nums[i] >= len(nums):
        nums[i] = 0
j = 0
while j < len(nums):
    if nums[0] > 0 and nums[nums[0]] > -1:
        temp = nums[nums[0]]
        nums[nums[0]] = -1
        nums[0] = temp
    else:
        while j < len(nums):
            if nums[j] > 0:
                nums[0] = nums[j]
                j += 1
                break
            j += 1
i = 0
for i in range(1, len(nums)):
    if nums[i] > -1:
        print(i)
    i += 1
print(i)