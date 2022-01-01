# Solution 1 [Using Sets]
nums = [1, 2, 3, 1]
def containsDuplicate(nums):
    return len(nums) > len(set(nums))
print(containsDuplicate(nums))

#Solution 2 [Using Counter]
from collections import Counter
def containsDuplicate1(nums):
    nums = dict(Counter(nums))
    for key, value in nums.items():
        if value > 1:
            return True
    return False
print(containsDuplicate1(nums))

