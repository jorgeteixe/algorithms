def odd(n):
    return n % 2 == 1


def even(n):
    return n % 2 == 0


def binary_gcd(a, b):
    if a < 0 or b < 0:
        raise ArithmeticError('Numbers must be positive.')
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if even(a):
        if odd(b):
            return binary_gcd(a / 2, b)
        else:
            return 2 * binary_gcd(a / 2, b / 2)
    else:
        if even(b):
            return binary_gcd(a, b / 2)
        if a > b:
            return binary_gcd((a - b) / 2, b)
        else:
            return binary_gcd((b - a) / 2, a)


def main():
    a = 12
    b = 20
    gcd = binary_gcd(a, b)
    print(f'gcm({a}, {b}) = {"%d" % gcd}')


if __name__ == '__main__':
    main()
