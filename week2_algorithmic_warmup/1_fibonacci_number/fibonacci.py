# Uses python3
def calc_fib(n):
    a, b, c = 0, 1, 0
    if n == 1 :
        return 1
    while n > 1:
        c = a + b
        a, b = b, c
        n = n-1
    return c


a, b = map(int, input().split())
print(calc_fib(a)% b)
