# Solution
matrix = [[1,1,1],[1,0,1],[1,1,1]]
firstRowZero = False
firstColZero = False
r = len(matrix)
c = len(matrix[0])
for i in range(0, c):
    if matrix[0][i] == 0:
        firstRowZero = True
        break
for i in range(0, r):
    if matrix[i][0] == 0:
        firstColZero = True
        break
for i in range(1, r):
    for j in range(1, c):
        if matrix[i][j] == 0:
            matrix[0][j] = 0
            matrix[i][0] = 0
for i in range(1, r):
    for j in range(1, c):
        if matrix[0][j] == 0 or matrix[i][0] == 0:
            matrix[i][j] = 0
if firstRowZero:
    for i in range(0, c):
        matrix[0][i] = 0
if firstColZero:
    for i in range(0, r):
        matrix[i][0] = 0
print(matrix)