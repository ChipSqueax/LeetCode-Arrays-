# Solution
nums = [100, 1, 200, 3, 4, 2]
length = 0
mySet = set(nums)
for item in mySet:
    if item-1 not in mySet:
        y = item + 1
        while y in mySet:
            y += 1
        length = max(length, y-item)
print(length)