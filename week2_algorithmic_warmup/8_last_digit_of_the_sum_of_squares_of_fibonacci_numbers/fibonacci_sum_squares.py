# Uses python3

def next_fib():
    p, c = 0, 1
    yield p
    yield c
    while True:
        p, c = c, p + c
        yield c


def pisano_seq(m):
    def check(cand):
        middle = len(cand) // 2
        if middle == 0:
            return False
        for i in range(middle):
            if cand[i] != cand[middle + i]:
                return False
        return True

    seq = []
    for fib in next_fib():
        seq.append(fib % m)
        if (len(seq) % 2):
            if check(seq):
                return seq[:len(seq) // 2]


def last_digits(n):
    seq = pisano_seq(10)
    return seq[n % len(seq)], seq[(n + 1) % len(seq)]


def sum_sq(n):
    p, c = last_digits(n)
    return (p * c) % 10


if __name__ == '__main__':
    n = int(input())
    result = sum_sq(n)
    print(result)