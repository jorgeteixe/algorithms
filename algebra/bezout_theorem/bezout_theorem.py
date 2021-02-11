from algebra.extended_euclidean_algorithm.extended_euclidean_algorithm import extended_euclidean_algorithm


def main():
    a = 72
    b = -23
    gcd, r, s = extended_euclidean_algorithm(a, b)
    print(f'gcd({a}, {b}) = {gcd} = {r}x{a} + {s}x{b} ')


if __name__ == '__main__':
    main()
