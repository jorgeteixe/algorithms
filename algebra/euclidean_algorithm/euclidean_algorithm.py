def euclidean_algorithm(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a


def main():
    a = 252
    b = 105
    gcd = euclidean_algorithm(a, b)
    print(f'gcd({a}, {b}) = {gcd}')


if __name__ == '__main__':
    main()
