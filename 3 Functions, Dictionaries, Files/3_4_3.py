Dictionary = {}
res = []
with open('dataset_3363_3.txt') as inf:
    for line in inf:
        for i in line.lower().split():
            if i in Dictionary.keys():
                Dictionary[i] += 1
            else:
                Dictionary[i] = 1

maximum = max(Dictionary.values())
for i in Dictionary.keys():
    if Dictionary[i] == maximum:
        res.append(i)

res_str = min(res) + ' ' + str(maximum)

with open('res.txt','w') as ouf:
    ouf.write(res_str)