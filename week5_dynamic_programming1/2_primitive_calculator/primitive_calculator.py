# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    a = [0]*(n+1)
    for i in range(1, n+1):
        a[i] = a[i-1] + 1;
        if i % 2 == 0:
            a[i] = min(a[i//2]+1, a[i])
        if i % 3 == 0:
            a[i] = min(a[i//3]+1, a[i])

    while n >= 1:
        sequence.append(n)
        if a[n] == a[n-1] + 1:
            n = n - 1
        elif n % 2 == 0 and a[n//2] == a[n] - 1:
            n = n // 2
        elif n % 3 == 0 and a[n//3] == a[n] - 1:
            n = n // 3

    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')