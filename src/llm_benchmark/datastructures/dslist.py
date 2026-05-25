from typing import List


class DsList:
    @staticmethod
    def modify_list(v: List[int]) -> List[int]:
        return [x + 1 for x in v]

    @staticmethod
    def search_list(v: List[int], n: int) -> List[int]:
        return [i for i, x in enumerate(v) if x == n]

    @staticmethod
    def sort_list(v: List[int]) -> List[int]:
        return sorted(v)

    @staticmethod
    def reverse_list(v: List[int]) -> List[int]:
        return v[::-1]

    @staticmethod
    def rotate_list(v: List[int], n: int) -> List[int]:
        n = n % len(v)  # Ensure n is within the bounds of the list length
        return v[n:] + v[:n]

    @staticmethod
    def merge_lists(v1: List[int], v2: List[int]) -> List[int]:
        return v1 + v2