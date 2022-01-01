# LeetCode-Arrays-

### Contains Duplicate
[Problem](https://leetcode.com/problems/contains-duplicate/)
The first solution uses sets to check if both the array and set have the same number of elements...
Since, if the set has lesser elements, the array for sure contains duplicates.
The second solution uses a dictionary to store the frequency of each element and checks if their frequencies are > 1.
Both solutions run at approximately O(n) but the second one had a slightly better time and space complexity.
