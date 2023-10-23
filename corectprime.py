def sieve_of_eratosthenes(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False

    for p in range(2, n + 1):
        if p * p <= n and isPrime[p]:
            for i in range(p * 2, n + 1, p):
                isPrime[i] = False

    return isPrime


def superPrimes(n):
    isPrime = sieve_of_eratosthenes(n)
    primes = [p for p in range(2, n + 1) if isPrime[p]]

    for prime in primes:
        if isPrime[prime]:
            print(prime, end=" ")


n = 241
print("Super-Primes less than or equal to", n, "are:")
superPrimes(n)
