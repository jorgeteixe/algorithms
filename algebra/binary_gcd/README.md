# Binary GCD
## Definition
 Binary GCD algorithm:
 1. gcd(0, b) = b, because everything divides zero, and b is the largest number that divides b. Similarly, gcd(a, 0) = a.
 2. gcd(2a, 2b) = 2·gcd(a, b)
 3. gcd(2a, b) = gcd(a, b), if b is odd (2 is not a common divisor). Similarly, gcd(a, 2b) = gcd(a, b) if a is odd.
 4. gcd(a, b) = gcd(|a − b|, min(a, b)), if a and b are both odd.

> You can find a detailed explanation [here](https://en.wikipedia.org/wiki/Binary_GCD_algorithm).