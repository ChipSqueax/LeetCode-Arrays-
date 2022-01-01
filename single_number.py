# Solution 1
nums = [2, 2, 1]
val = 0
for i in range(len(nums)):
    val = val ^ nums[i]
print(val)
