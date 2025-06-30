from typing import List


class DoubleForLoop:
    @staticmethod
    def sum_square(n: int) -> int:

        sum_ = 0
        for i in range(n):
            sum_ += i * i
        return sum_

    @staticmethod
    def sum_triangle(n: int) -> int:
        """Sum of triangle of numbers from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of triangle of numbers from 0 to n
        """
        sum_ = 0
        for i in range(n):
            sum_ += (i * (i + 1)) // 2
        return sum_

    @staticmethod
    def count_pairs(arr: List[int]) -> int:
        """Count pairs of numbers in an array

        A pair is defined as exactly two numbers in the array that are equal.

        Args:
            arr (List[int]): Array of integers

        Returns:
            int: Number of pairs in the array
        """
        from collections import Counter
        count = 0
        freq = Counter(arr)
        for val in freq.values():
            if val == 2:
                count += 1
        return count

    @staticmethod
    def count_duplicates(arr0: List[int], arr1: List[int]) -> int:
        """Count duplicates between two arrays

        Args:
            arr0 (List[int]): Array of integers
            arr1 (List[int]): Array of integers

        Returns:
            int: Number of duplicates between the two arrays
        """
        count = 0
        seen = set(arr0)
        for num in arr1:
            if num in seen:
                count += 1
                seen.remove(num)  # Ensure each duplicate is only counted once
        return count

    @staticmethod
    def sum_matrix(m: List[List[int]]) -> int:
        """Sum of matrix of integers

        Args:
            m (List[List[int]]): Matrix of integers

        Returns:
            int: Sum of matrix of integers
        """
        sum_ = 0
        for row in m:
            sum_ += sum(row)
        return sum_