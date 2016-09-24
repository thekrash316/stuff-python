def next_prime(n):
    '''
    >>> next_prime(-2)
    -1
    >>> next_prime(-1)
    0
    >>> next_prime(0)
    1
    >>> next_prime(1)
    2
    >>> next_prime(2)
    3
    >>> next_prime(3)
    5
    >>> next_prime(6)
    7
    >>> next_prime(7)
    11
    >>> next_prime(25)
    29
    >>> next_prime(22)
    23
    >>> next_prime(78)
    79
    >>> next_prime(100)
    -1
    '''

    first = n + 1

    if first < 0 and first >= 100:
        return -1

    for x in range(first, 100):
        if is_prime(x):
            return x

    return -1


def is_prime(n):
    if n >= 0 and n <= 2:
        return True

    for x in range(2, n / 2 + 1):
        if (n % x) == 0:
            return False

    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()

