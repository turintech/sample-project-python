from sys import maxsize
from typing import List


from sys import maxsize
from typing import List


class Sort:
    @staticmethod
    def sort_list(v: List[int]) -> None:
        """
        Sort a list of integers in place

        Args:
            v (List[int]): List of integers
        """
        v.sort()

    @staticmethod
    def dutch_flag_partition(v: List[int], pivot_value: int) -> None:
        """
        Dutch flag partitioning

        Args:
            v (List[int]): List of integers
            pivot_value (int): Pivot value
        """
        low = 0
        mid = 0
        high = len(v) - 1

        while mid <= high:
            if v[mid] < pivot_value:
                v[low], v[mid] = v[mid], v[low]
                low += 1
                mid += 1
            elif v[mid] == pivot_value:
                mid += 1
            else:
                v[mid], v[high] = v[high], v[mid]
                high -= 1

    @staticmethod
    def max_n(v: List[int], n: int) -> List[int]:
        """
        Find the maximum n numbers in a list

        Args:
            v (List[int]): List of integers
            n (int): Number of maximum values to find

        Returns:
            List[int]: List of maximum n values
        """
        v.sort()
        return v[-n:]