Length = int(input())
Res_list = []
for i in range(10000000000000000000000):
    if len(Res_list) < Length:
        Res_list.extend([i]*i)
    else:
        break
for k in Res_list[:Length]:
    print(int(k), end=" ")