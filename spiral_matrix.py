# Solution 1
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
output = []
while matrix:
    output += matrix[0]
    matrix = list(zip(*matrix[1:]))[::-1]
print(output)

# Solution 2
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
r = len(matrix[0])
d = len(matrix)
m = r
n = d
l = 0
u = 0
i = 0
j = 0
direction = 0
output = []
count = 0
while count < m*n:
    if direction == 0:
        while j < r:
            output.append(matrix[i][j])
            count += 1
            j += 1
        j -= 1
        i += 1
        u += 1            
    elif direction == 1:
        while i < d:
            output.append(matrix[i][j])
            count += 1
            i += 1
        i -= 1
        j -= 1
        r -= 1
    elif direction == 2:
        while j >= l:
            output.append(matrix[i][j])
            count += 1
            j -= 1
        j += 1
        i -= 1
        d -= 1
    elif direction == 3:
        while i >= u:
            output.append(matrix[i][j])
            count += 1
            i -= 1
        i += 1
        j += 1
        l += 1
    direction = (direction+1)%4
print(output)