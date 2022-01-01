nums = [4,3,2,7,8,2,3,1]
# Solution 1
i = 0
while i < len(nums):
    num = abs(nums[i])
    nums[num-1] = -abs(nums[num-1])
    i+=1
output = []
for i in range(len(nums)):
    if nums[i] > 0:
        output.append(i+1)
print(output)
