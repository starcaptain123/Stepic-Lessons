import requests
url = "https://stepic.org/media/attachments/course67/3.6.3/"

with open('test.txt') as inf:
    link = inf.readline().strip()

newlink = str(requests.get(link).text)
print(newlink)
while newlink[:2] != 'We':
    newlink = requests.get((url+newlink)).text
    print(newlink[:2])
print(newlink)