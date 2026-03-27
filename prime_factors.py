def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    factors = prime_factors(number)
    print(f"Prime factors of {number}: {' x '.join(map(str, factors))}")
