from typing import List


class SingleForLoop:
    @staticmethod
    def sum_range(n: int) -> int:
        """Sum of range of numbers from 0 to n

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of range of numbers from 0 to n
        """
        return (n * (n - 1)) // 2

    @staticmethod
    def max_list(v: List[int]) -> int:
        """Maximum value in a vector

        Args:
            v (List[int]): Vector of integers

        Returns:
            int: Maximum value in the vector
        """
        return max(v) if v else 0

    @staticmethod
    def sum_modulus(n: int, m: int) -> int:
        """Sum of modulus of numbers from 0 to n

        Args:
            n (int): Number to sum up to
            m (int): Modulus

        Returns:
            int: Sum of modulus of numbers from 0 to n
        """
        sum_val = 0
        for i in range(0, n, m):
            sum_val += i
        return sum_val