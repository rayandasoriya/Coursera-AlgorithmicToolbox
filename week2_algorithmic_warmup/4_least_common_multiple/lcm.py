# Uses python3
from __future__ import division
import sys


def gcd_naive(a, b):
    if b == 0:
        return a
    else:
        return gcd_naive(b, a % b)


def lcm_naive(a, b):
    return int((a*b)//gcd_naive(a, b))


a, b = map(int, input().split())
print(lcm_naive(a, b))