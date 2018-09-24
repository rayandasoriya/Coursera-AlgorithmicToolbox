# python3

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

m1 = max(a)
a.remove(m1)
m2 = max(a)
print(m1*m2)
