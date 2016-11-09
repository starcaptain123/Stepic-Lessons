n, k = map(int, input().split())


def c(a, b):
    if b == 0:
        result = 1
    elif b > a:
        result = 0
    else:
        result = c(a - 1, b) + c(a - 1, b - 1)
    return result


print(c(n, k))