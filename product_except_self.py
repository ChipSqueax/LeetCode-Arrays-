nums = [1, 2, 3, 4]
# Solution 1
output = [1 for i in range(len(nums))]
n = len(nums)
left_prod = 1
for i in range(1, n):
    left_prod *= nums[i-1]
    output[i] *= left_prod
right_prod = 1
for i in reversed(range(0, n-1)):
    right_prod *= nums[i+1]
    output[i] *= right_prod
print(output)