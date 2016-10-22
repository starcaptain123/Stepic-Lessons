def modify_list(l):
    k = 0
    for i in range(len(l)):
        if l[i] % 2 == 1:
            l[i] = "+"
            k += 1
        else:
            l[i] //= 2
    while k != 0:
        l.remove("+")
        k -= 1

