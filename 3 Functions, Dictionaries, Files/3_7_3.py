d = int(input()) # кол-во слов в словаре
Dictionary = [] # словарь
Text = []
result = []
for i in range(d):
    Dictionary.append(input().lower())
l = int(input()) # кол-во строк текста
for k in range(l):
    List = [i for i in input().lower().split()]
    Text.extend(List)

for i in range(len(Text)):
    if Text[i] not in Dictionary and Text[i] not in result:
        result.append(Text[i])

for i in result:
    print(i)