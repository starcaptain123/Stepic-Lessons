Dict = {'север': [1, 1], 'юг': [1, -1], 'восток': [0, 1], 'запад': [0, -1]}
result = [0, 0]
n = int(input())
for i in range(n):
    line = [i for i in input().split()]
    result[Dict[line[0]][0]] += int(line[1])*Dict[line[0]][1]
for i in result:
    print(i, end=" ")