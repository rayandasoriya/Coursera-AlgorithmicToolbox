# Uses python3


def get_change(m):
    no_ten, no_one, no_five = 0, 0, 0
    if m // 10 > 0:
        no_ten = m // 10
        m -= no_ten*10
    if m // 5 > 0:
        no_five = m // 5
        m -= no_five * 5
    if m // 1 > 0:
        no_one = m // 1
        m -= no_one * 1
    m = no_five + no_one + no_ten
    return m


print(get_change(int(input())))
