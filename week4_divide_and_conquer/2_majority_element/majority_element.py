# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_el = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    right_el = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    lcount = 0
    for i in range(left, right):
        if a[i] == left_el:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_el

    rcount = 0
    for i in range(left, right):
        if a[i] == right_el:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_el
    #write your code here
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
