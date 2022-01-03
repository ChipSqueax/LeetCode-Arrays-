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

### Product of array except self
[Problem](https://leetcode.com/problems/product-of-array-except-self/)

* The problem can be reframed as follows: At every index, place the product of all elements to the left of the index and the product of all elements to the right of the index. So, we first traverse through the list from left to right and place the product of all left elements. Then we traverse through the list from right to left and place the product of all right elements. Then we multiply the products at each index to obtain the required output.

### Duplicate number
[Problem](https://leetcode.com/problems/find-the-duplicate-number/)

* The indices lie in the range mentioned in the problem, the indices are sorted and the duplicate is one of the indices...what do we do?
Of course, we search for the duplicate in the indices using Binary Search.
If for any index mid, the number of elements > mid is > mid, then there definitely is a duplicate in the range from low to mid...else, the duplicate lies in the other range...

### Find all duplicate numbers
[Problem](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

* Same old trick of using the list itself as a hashmap. The corresponding index of a particular value is made negative and if we find that the value at a particular index is already negative, we know that it is a duplicate...

### Set matrix zeros
[Problem](https://leetcode.com/problems/set-matrix-zeroes/)

* We use the first row and the first column to store the zeros since these are the first cells to get filled anyway.
We then iterate through the rest of the cells and check if the first cell in the corresponding row or the first cell in the corresponding column is 0 as recorded earlier...based on this, we set the cell to 0.
But what if the first row and the first column themselves need to be set to 0s? To handle this, initially we store two booleans and after handling the rest of the cells, we handle the first row and first column through these booleans. 

### Spiral Matrix
[Problem](https://leetcode.com/problems/spiral-matrix/)

* P.S. This solution was presented by Stefan Pochamann in the Leetcode discuss section.
This is the most pythonic way of doing it. The first row of the matrix contains elements in the order that they are to be presented in the output. Then the remaining matrix is rotated 90 degrees counter-clockwise and the first row is added to the output and the process continues....till the matrix is not empty.

* This solution is a more naive solution where we traverse through the elements in the matrix in a spiral manner and reduce the boundaries throughout the traversal.

### Rotate matrix
[Problem](https://leetcode.com/problems/rotate-image/)

* First, reverse the matrix vertically and reverse the elements along the diagonal.

### Longest Consecutive Sequence
[Problem](https://leetcode.com/problems/longest-consecutive-sequence/)

* We first convert the list to a set which takes O(n) time. This is because, a set does not store duplicates and we can check if an element exists in a set in O(1) time.
We loop through each element in the set and find the end of the sequence starting from each element. the length of this sequence would be end - start + 1. We need to find the largest of such lengths.
To improve the algorithm, consider only the least number in each sequence, that is, ignore an element if an element lesser than it already exists in the set.

### First Missing Positive
[Problem](https://leetcode.com/problems/first-missing-positive/)

* First, add a dummy 0 to the list and then remove all dummies (negatives and positive numbers greater than the length of the list) because we cannot record them in the same list.
Next start recording every valid element in the list by making their corresponding index as -1. Use the 0th index for storing intermediate values. Next, loop through the elements from index 1 to the end. The first index which does not have 1 is the first positive value.! 

