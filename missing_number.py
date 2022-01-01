nums = [9,6,4,2,3,5,7,0,1]
# Solution 1 [Math formula]
n = len(nums)
print(n*(n+1)//2 - sum(nums))
# Solution 2 [Bit manipulation]
val = 0
for num in nums:
    val ^= num
for i in range(0, len(nums)+1):
    val ^= i
print(val)