# LeetCode-Arrays-

## Problem Set

[ProblemSet](https://seanprashad.com/leetcode-patterns/)

### Contains Duplicate
[Problem](https://leetcode.com/problems/contains-duplicate/)

* The first solution uses sets to check if both the array and set have the same number of elements...
Since, if the set has lesser elements, the array for sure contains duplicates.

* The second solution uses a dictionary to store the frequency of each element and checks if their frequencies are > 1.
Both solutions run at approximately O(n) but the second one had a slightly better time and space complexity.

### Missing Number 
[Problem](https://https://leetcode.com/problems/missing-number/)

* The easiest solution would be to find the sum of first n whole numbers and find the sum of the elements in the list. The difference between these two sums is the missing number.

* A very cool solution is to use the XOR operation. Initially, a variable is 0. Performing XOR twice on the variable always results in 0. Note that XOR can be applied in any order on the variable...
So, first we apply XOR for all the elements in the list and then for all numbers from 0 to n. Ideally, the variable should result in 0 but the missing number performs XOR only once so the variable has the value of the missing number.!!

### Disappeared Numbers
[Problem](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

* The list can be used as a hashmap and all the occured elements can be marked as negative. When iterating through the list, the indices which have positive elements haven't occured in the list.

* If we are to use bit manipulation, we can set the num-th bit of a variable initially 0. This can be done by ORing (1 << num) with the variable. While iterating over the range n, if we find an unset bit, add that into the output list. [this is done by ANDing (1 << num) with the variable].

### Single Number
[Problem](https://leetcode.com/problems/single-number/)

* The best solution uses bit manipulation (XOR). This problem is similar to Missing number and we can apply the same logic here. Every number performs XOR twice on the variable and only one number does it once...It is this number which gets stored in the variable.!
