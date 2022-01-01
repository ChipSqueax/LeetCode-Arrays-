nums = [9,6,4,2,3,5,7,0,1]
val = 0
for num in nums:
    val ^= num
for i in range(0, len(nums)+1):
    val ^= i
print(val)