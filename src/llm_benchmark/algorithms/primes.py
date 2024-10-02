from typing import List


class Primes:
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def sum_primes(n: int) -> int:
        """Sum of primes from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of primes from 0 to n
        """
        if n <= 1:
            return 0
        primes = [True] * n
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n, p):
                    primes[i] = False
            p += 1
        sum_ = 0
        for i in range(2, n):
            if primes[i]:
                sum_ += i
        return sum_

    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Prime factors of a number

        Args:
            n (int): Number to factorize

        Returns:
            List[int]: List of prime factors
        """
        ret = []
        i = 2
        while i * i <= n:
            while n % i == 0:
                ret.append(i)
                n //= i
            i += 1
        if n > 1:
            ret.append(n)
        return ret