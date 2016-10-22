res = []
lst = [int(i) for i in input().split()]
l = len(lst)
if l == 1:
    res = list(lst)
else:
    lst.append(lst[0])
    lst.insert(0, lst[l-1])
    for k in range(1, l+1):
        res.append(int(lst[k-1])+int(lst[k+1]))
for m in res:
    print(m, end=" ")