from heapq import nlargest

class Sort:
    @staticmethod
    def sort_list(v: List[int]) -> None:
        v.sort()

    @staticmethod
    def dutch_flag_partition(v: List[int], pivot_value: int) -> None:
        low, mid, high = 0, 0, len(v) - 1
        while mid <= high:
            if v[mid] < pivot_value:
                v[low], v[mid] = v[mid], v[low]
                low += 1
                mid += 1
            elif v[mid] > pivot_value:
                v[mid], v[high] = v[high], v[mid]
                high -= 1
            else:
                mid += 1

    @staticmethod
    def max_n(v: List[int], n: int) -> List[int]:
        return nlargest(n, v)