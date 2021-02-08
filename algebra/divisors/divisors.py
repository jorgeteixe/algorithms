from algebra.integer_division.integer_division import integer_division


def divisors(a):
    divs = []
    i = 1
    while i <= a:
        _, r = integer_division(+a, i)
        if r == 0:
            divs.append(i)
            divs.append(-i)
        i += 1
    return divs


def main():
    a = 100
    divs = divisors(a)
    print(f'a = {a}\ndivs = {divs}')


if __name__ == '__main__':
    main()
