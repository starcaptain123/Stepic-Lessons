n = int(input())
d = {}

for k in range(n):
    lst = [i for i in input().split(";")]

    # Обработка итогов матча для 1 команды:
    if lst[0] in d.keys():
        d[lst[0]][0] += 1
    else:
        d.update({lst[0]: [1, 0, 0, 0, 0]})

    if int(lst[1]) > int(lst[3]):
        d[lst[0]][1] += 1
    elif int(lst[1]) == int(lst[3]):
        d[lst[0]][2] += 1
    elif int(lst[1]) < int(lst[3]):
        d[lst[0]][3] += 1

    d[lst[0]][4] = (d[lst[0]][1])*3 + (d[lst[0]][2])

    # Обработка итогов матча для 2 команды:

    if lst[2] in d.keys():
        d[lst[2]][0] += 1
    else:
        d.update({lst[2]: [1, 0, 0, 0, 0]})

    if int(lst[3]) > int(lst[1]):
        d[lst[2]][1] += 1
    elif int(lst[3]) == int(lst[1]):
        d[lst[2]][2] += 1
    elif int(lst[3]) < int(lst[1]):
        d[lst[2]][3] += 1

    d[lst[2]][4] = (d[lst[2]][1]) * 3 + (d[lst[2]][2])

for m in d.keys():
    print(m, end=":")
    for n in d[m]:
        print(n, end=' ')
    print('')