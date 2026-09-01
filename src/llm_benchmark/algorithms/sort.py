from heapq import nlargest
from typing import List


class Sort:
    @staticmethod
    def sort_list(v: List[int]) -> None:
        """Sort a list of integers in place

        Args:
            v (List[int]): List of integers
        """
        v.sort()

    @staticmethod
    def dutch_flag_partition(v: List[int], pivot_value: int) -> None:
        """Dutch flag partitioning

        Args:
            v (List[int]): List of integers
            pivot_value (int): Pivot value
        """
        next_value = 0

        for i in range(len(v)):
            if v[i] < pivot_value:
                v[i], v[next_value] = v[next_value], v[i]
                next_value += 1
        for i in range(next_value, len(v)):
            if v[i] == pivot_value:
                v[i], v[next_value] = v[next_value], v[i]
                next_value += 1

    @staticmethod
    def max_n(v: List[int], n: int) -> List[int]:
        """Find the maximum n numbers in a list

        Args:
            v (List[int]): List of integers
            n (int): Number of maximum values to find

        Returns:
            List[int]: List of maximum n values
        """
        return nlargest(n, v)
