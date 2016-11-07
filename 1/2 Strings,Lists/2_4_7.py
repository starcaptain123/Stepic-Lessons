s = input()
temps = s+'+'
k = 1
tmp = temps[0]
res=""
for i in temps[1:]:
    if i == tmp:
        k += 1
        tmp = i
    else:
        res += tmp+str(k)
        k = 1
        tmp = i
print(res)