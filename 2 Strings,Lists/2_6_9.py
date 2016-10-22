lst = [int(i) for i in input().split()]
x = int(input())
count = int(lst.count(x))
res_lst = []
i = count-1
if count == 0:
    print("Отсутствует")
else:
    while i >= 0:
        res_lst.append(lst.index(x))
        lst[lst.index(x)] = "+"
        i -= 1
for i in res_lst:
    print(i, end=" ")