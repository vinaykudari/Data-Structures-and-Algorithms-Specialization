# Uses python3
def fib(n):
    lis = [0, 1]
    if n <= 1:
        return lis[n]
    else:
        for i in range(1, n):
            lis.append(lis[i - 1] + lis[i])
        return lis[n]


n = int(input())
print(fib(n))
