import requests
with open('test.txt') as inf:
    line = inf.readline().strip()
file = requests.get(url=line).text
k = 0
for i in file.splitlines():
    k += 1
print(k)