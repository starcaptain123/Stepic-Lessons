Sum = int(input())
Sum_kv = Sum*Sum
while Sum != 0:
    i = int(input())
    Sum += i
    Sum_kv += i*i
print(Sum_kv)