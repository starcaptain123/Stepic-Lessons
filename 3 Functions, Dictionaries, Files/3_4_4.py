Result = ''
d = {'name': '', 'math': 0, 'phys': 0, 'rus': 0}
math_all = 0
phys_all = 0
rus_all = 0
k = 0
with open('test.txt') as inf:
    for line in inf:
        line = line.strip().split(';')
        d['name'] = line[0]
        d['math'] = int(line[1])
        d['phys'] = int(line[2])
        d['rus'] = int(line[3])
        res = str((d['math']+d['phys']+d['rus'])/3)
        Result += res + '\n'
        math_all += d['math']
        phys_all += d['phys']
        rus_all += d['rus']
        k += 1
Result += str(math_all/k) + " " + str(phys_all/k) + " " + str(rus_all/k)
with open('res.txt', 'w') as ouf:
    ouf.write(Result)
