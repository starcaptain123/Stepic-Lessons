res1 = ""
res2 = ""
i = 0
with open("test.txt") as inf:
    line = inf.readline().strip()
    while i < len(line):
        if line[i].isalpha():
            res1 += " " + line[i]
            i += 1
        else:
            res1 += line[i]
            i += 1

for i in res1.split():
    res2 += i[0]*int(i[1:])

with open("res.txt", 'w') as ouf:
    ouf.write(res2)