def sieve_of_eratosthenes(n):
    if n < 1:
        raise AttributeError('n has to be greater than 1')
    is_prime = [True] * n
    i = 2
    while i * i < n:
        if is_prime[i]:
            j = i * i
            while j < n:
                is_prime[j] = False
                j += i
        i += 1
    return [i for i in range(1, len(is_prime)) if is_prime[i]]


def main():
    n = 100
    primes = sieve_of_eratosthenes(n)
    print(f'primes = {primes}')


if __name__ == '__main__':
    main()
