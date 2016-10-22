lst = [int(i) for i in input().split()]
res = ""
#lst = [658, 123, -22, 109, 658, 123, 4, 4, 658]
lst.sort()
lst.append("+")
tmp = lst[0]
k=0
for i in lst[1:]:
    if i == tmp:
        tmp = i
        k += 1
    else:
        if k != 0:
            res += (str(tmp) + " ")
            tmp = i
            k = 0
        else:
            tmp = i
            k = 0
print(res)