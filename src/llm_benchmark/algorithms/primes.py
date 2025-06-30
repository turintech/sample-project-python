from typing import List
import math
import random


class Primes:
    @staticmethod
    def is_prime(n: int) -> bool:

        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def sum_primes(n: int) -> int:

        sum_ = 0
        for i in range(2, n):
            if Primes.is_prime(i):
                sum_ += i
        return sum_

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Compute the greatest common divisor of a and b."""
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def pollards_rho(n: int) -> int:
        """Pollard's Rho algorithm to find a non-trivial factor of n."""
        if n % 2 == 0:
            return 2
        x = random.randint(2, n - 1)
        y = x
        c = random.randint(1, n - 1)
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = Primes.gcd(abs(x - y), n)
            if d == n:
                return Primes.pollards_rho(n)
        return d

    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Prime factors of a number

        Args:
            n (int): Number to factorize

        Returns:
            List[int]: List of prime factors
        """
        if n <= 1:
            return []
        factors = []
        while n > 1:
            if Primes.is_prime(n):
                factors.append(n)
                break
            factor = Primes.pollards_rho(n)
            while n % factor == 0:
                factors.append(factor)
                n //= factor
        return factors