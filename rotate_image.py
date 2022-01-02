# Solution
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
n = len(matrix)
for i in range(n//2):
    for j in range(n):
        matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        
i = 0
while i < n:
    j = i
    while j < n:
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        j += 1
    i += 1
print(matrix)