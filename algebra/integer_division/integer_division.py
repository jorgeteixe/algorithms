def integer_division(a, b):
    if b == 0:
        raise ArithmeticError('Cannot divide by 0.')
    q = 0
    r = a
    while r >= b:
        q += 1
        r = r - b
    return q, r


def main():
    a = 60
    b = 7
    q, r = integer_division(a, b)
    print(f'a = {a}\nb = {b}\nq = {q}\nr = {r}')
    print(f'{a} = {b}*{q} + {r}')


if __name__ == '__main__':
    main()
