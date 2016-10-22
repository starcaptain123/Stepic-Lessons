inp = input()
matrix = []
while inp != "end":
    matrix.append([int(i) for i in str(inp).split()])
    inp = input()


x = len(matrix)
y = len(matrix[0])

for i in range(x):
    for j in range(y):
        element = matrix[i-1][j] + matrix[i+1-x][j] + matrix[i][j+1-y] + matrix[i][j-1]
        print(element, end=" ")
    print()