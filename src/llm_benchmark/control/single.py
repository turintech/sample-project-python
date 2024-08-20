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
        arr = []
        for i in range(n):
            arr.append(i)
        return sum(arr)

    @staticmethod
    def max_list(v: List[int]) -> int:
        """Maximum value in a vector

        Args:
            v (List[int]): Vector of integers

        Returns:
            int: Maximum value in the vector
        """
        max_val = v[0]
        for i in range(1, len(v)):
            if v[i] > max_val:
                max_val = v[i]
        return max_val

    @staticmethod
    def sum_modulus(n: int, m: int) -> int:
        """Sum of modulus of numbers from 0 to n

        Args:
            n (int): Number to sum up to
            m (int): Modulus

        Returns:
            int: Sum of modulus of numbers from 0 to n
        """
        arr = []
        for i in range(n):
            if i % m == 0:
                arr.append(i)
        return sum(arr)
