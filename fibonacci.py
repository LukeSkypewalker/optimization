def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    f = [0] * (n + 1)
    f[0] = 1
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f


# print(fib(4))
print(fibonacci(4))
