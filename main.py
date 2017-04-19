# -*- ccoding: utf8 -*-


def gcd(a, b):

    m = a % b

    while m > 0:
        a = b
        b = m
        m = a % b

    return b


def gcd2(a, b):

    if a % b == 0:
        return b
    else:
        return gcd2(b, a % b)


def test():

    assert gcd(5, 10) == gcd2(5, 10) == 5
    assert gcd(77, 66) == gcd2(77, 66) == 11
    assert gcd(12, 18) == gcd2(12, 18) == 6

    print "Success"


def main():

    pass


if __name__ == "__main__":
    test()
    #main()
