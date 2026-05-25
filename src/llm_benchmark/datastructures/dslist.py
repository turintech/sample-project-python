from typing import List


class DsList:
    @staticmethod
    def modify_list(v: List[int]) -> List[int]:
        """Modify a list by adding 1 to each element

        Args:
            v (List[int]): List of integers

        Returns:
            List[int]: Modified list of integers
        """
        ret = []
        for i in range(len(v)):
            ret.append(v[i] + 1)
        return ret

    @staticmethod
    def search_list(v: List[int], n: int) -> List[int]:
        """Search a list for a value, returning a list
        of indices where the value is found

        Args:
            v (List[int]): List of integers
            n (int): Value to search for

        Returns:
            List[int]: List of indices where the value is found
        """
        ret = []
        for i in range(len(v)):
            if v[i] == n:
                ret.append(i)
        return ret

    @staticmethod
    def sort_list(v: List[int]) -> List[int]:
        """Sort a list of integers, returns a copy

        Args:
            v (List[int]): List of integers

        Returns:
            List[int]: Sorted list of integers
        """
        ret = v.copy()
        for i in range(len(ret)):
            for j in range(i + 1, len(ret)):
                if ret[i] > ret[j]:
                    ret[i], ret[j] = ret[j], ret[i]

        return ret

    @staticmethod
    def reverse_list(v: List[int]) -> List[int]:
        """Reverse a list of integers, returns a copy

        Args:
            v (List[int]): List of integers

        Returns:
            List[int]: Reversed list of integers
        """
        ret = []
        for i in range(len(v)):
            ret.append(v[len(v) - 1 - i])
        return ret

    @staticmethod
    def rotate_list(v: List[int], n: int) -> List[int]:
        """Rotate a list of integers by n positions

        Args:
            v (List[int]): List of integers
            n (int): Number of positions to rotate

        Returns:
            List[int]: Rotated list of integers
        """
        if len(v) == 0:
            return []
        n = n % len(v)
        ret = []
        for i in range(n, len(v)):
            ret.append(v[i])
        for i in range(n):
            ret.append(v[i])
        return ret

    @staticmethod
    def merge_lists(v1: List[int], v2: List[int]) -> List[int]:
        """Merge two lists of integers, returns a copy

        Args:
            v1 (List[int]): First list of integers
            v2 (List[int]): Second list of integers

        Returns:
            List[int]: Merged list of integers
        """
        ret = []
        for i in range(len(v1)):
            ret.append(v1[i])
        for i in range(len(v2)):
            ret.append(v2[i])
        return ret
