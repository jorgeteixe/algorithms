def print_euclidean_table(n, q, r, s):
    print(f' i    n   q   r   s')
    print(f'{"%2d" % 0}{"%5d" % n[0]}   -{"%4d" % r[0]}{"%4d" % s[0]}')
    for i in range(1, len(n) - 1):
        print(f'{"%2d" % i}{"%5d" % n[i]}{"%4d" % q[i]}{"%4d" % r[i]}{"%4d" % s[i]}')
    print(f'{"%2d" % (len(n) - 1)}{"%5d" % n[len(n) - 1]}   -   -   - \n')


def extended_euclidean_algorithm(a, b, table=False):
    n = [abs(a), abs(b)]
    q = [-1]
    r = [1, 0]
    s = [0, 1]
    q.append(int(n[0] / n[1]))
    i = 2
    while n[i - 1] != 0:
        n.append(n[i - 2] % n[i - 1])
        if n[i] == 0:
            break
        q.append(int(n[i - 1] / n[i]))
        r.append(r[i - 2] - q[i - 1] * r[i - 1])
        s.append(s[i - 2] - q[i - 1] * s[i - 1])
        i += 1
    if table:
        print_euclidean_table(n, q, r, s)
    final_r = r[len(r) - 1]
    final_s = s[len(s) - 1]
    if a < 0:
        final_r = -final_r
    if b < 0:
        final_s = -final_s
    return n[len(n) - 2], final_r, final_s


def main():
    a = 72
    b = -23
    gcd, _, _ = extended_euclidean_algorithm(a, b, table=True)
    print(f'gcd({a}, {b}) = {gcd}')


if __name__ == '__main__':
    main()
