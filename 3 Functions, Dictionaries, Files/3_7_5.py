Dict = {str(i): [0, 0, '-'] for i in range(1,12)}
with open('test.txt') as inf:
    for line in inf:
        line = line.strip().split('\t')
        Dict[line[0]][0] += int(line[2])
        Dict[line[0]][1] += 1
        Dict[line[0]][2] = Dict[line[0]][0]/Dict[line[0]][1]
for i in range(1,12):
    print(i, (Dict[str(i)][2]))