# Solution
nums = [4,3,2,7,8,2,3,1]
output = []
for num in nums:
    if nums[abs(num) - 1] < 0:
        output.append(abs(num))
    else:
        nums[abs(num) - 1] *= -1
print(output)