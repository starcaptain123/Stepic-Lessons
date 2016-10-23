n = int(input())
dictionary = {}
for i in range(n):
    x = int(input())
    if x in dictionary.keys():
        print(dictionary[x])
    else:
        y = f(x)
        dictionary[x] = y
        print(y)