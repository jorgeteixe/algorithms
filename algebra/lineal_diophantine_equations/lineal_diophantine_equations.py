from algebra.extended_euclidean_algorithm.extended_euclidean_algorithm import extended_euclidean_algorithm


def diophantine_equation(a, b, n, equations=False):
    gcd, r, s = extended_euclidean_algorithm(a, b)
    if n % gcd != 0:
        print('Theese values doesn\'t have solution.')
        return None, None
    x0 = r/gcd*n
    y0 = s/gcd*n
    xt = b/gcd
    yt = a/gcd
    if equations:
        print(f'x = {"%d" % x0} + {"%d" % xt}t')
        print(f'y = {"%d" % y0} - {"%d" % yt}t')
    return x0, y0


def main():
    a = 72
    b = 23
    n = -4
    x0, y0 = diophantine_equation(a, b, n, equations=True)
    if x0 is None:
        return
    print(f'\nx0 = {"%d" % x0}')
    print(f'y0 = {"%d" % y0}')


if __name__ == '__main__':
    main()
