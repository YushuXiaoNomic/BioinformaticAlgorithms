def recursive_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        a = recursive_fibonacci(n - 1)
        b = recursive_fibonacci(n - 2)
        return a + b


def fibonacci(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.insert(i, f[i - 1] + f[i - 2])
    return f[n]


print(recursive_fibonacci(10))
print(fibonacci(10))
