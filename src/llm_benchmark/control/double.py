import collections
from typing import List


class DoubleForLoop:
    @staticmethod
    def sum_square(n: int) -> int:
        '''Sum of squares of numbers from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of squares of numbers from 0 to n
        '''
        return sum(i * i for i in range(n))

    @staticmethod
    def sum_triangle(n: int) -> int:
        '''Sum of triangle of numbers from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of triangle of numbers from 0 to n
        '''
        return sum(sum(range(i + 1)) for i in range(n))

    @staticmethod
    def count_pairs(arr: list[int]) -> int:
        '''Count pairs of numbers in an array

        A pair is defined as exactly two numbers in the array that are equal.

        Args:
            arr (List[int]): Array of integers

        Returns:
            int: Number of pairs in the array
        '''
        from collections import Counter
        return sum(count // 2 for count in Counter(arr).values() if count == 2)

    @staticmethod
    def count_duplicates(arr0: list[int], arr1: list[int]) -> int:
        '''Count duplicates between two arrays

        Args:
            arr0 (List[int]): Array of integers
            arr1 (List[int]): Array of integers

        Returns:
            int: Number of duplicates between the two arrays
        '''
        return sum(a == b for a, b in zip(arr0, arr1))

    @staticmethod
    def sum_matrix(m: list[list[int]]) -> int:
        '''Sum of matrix of integers

        Args:
            m (List[List[int]]): Matrix of integers

        Returns:
            int: Sum of matrix of integers
        '''
        return sum(sum(row) for row in m)