# Uses python3
def get_fibonacci_last_digit_naive(n):
    a, b, c = 0, 1, 0
    if n == 1:
        return 1
    while n > 1:

        c = a + b
        a, b = b, c % 10
        n = n-1

    return c % 10


n = int(input())
print(get_fibonacci_last_digit_naive(n))
