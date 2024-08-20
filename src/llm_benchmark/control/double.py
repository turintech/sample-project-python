from typing import List


class DoubleForLoop:
    @staticmethod
    def sum_square(n: int) -> int:
        """Sum of squares of numbers from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of squares of numbers from 0 to n
        """
        sum_ = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    sum_ += i * j
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
            for j in range(i + 1):
                sum_ += j
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
        count = 0
        for i in range(len(arr)):
            ndup = 0
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    ndup += 1
            if ndup == 2:
                count += 1

        return count // 2

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
        for i in range(len(arr0)):
            for j in range(len(arr1)):
                if i == j and arr0[i] == arr1[j]:
                    count += 1
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
        for i in range(len(m)):
            for j in range(len(m[i])):
                sum_ += m[i][j]
        return sum_
