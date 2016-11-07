Dictionary = {}
for i in input().split():
    if i in Dictionary:
        Dictionary[i] += 1
    else:
        Dictionary[i] = 1
for key, value in Dictionary.items():
    print(key, value)
