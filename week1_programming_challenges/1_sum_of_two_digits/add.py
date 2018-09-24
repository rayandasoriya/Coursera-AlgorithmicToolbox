#Using Python3
n = int(input())
a = [int(x) for x in input().split()]
x=max(a)
x1=a.index(max(a))
a.pop(x1)
y=max(a)
print (x*y)