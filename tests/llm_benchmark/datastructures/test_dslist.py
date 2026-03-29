from typing import List

import pytest

from llm_benchmark.datastructures.dslist import DsList


@pytest.mark.parametrize(
    "v, ref",
    [
        ([0], [1]),
        ([1, 2, 3], [2, 3, 4]),
        ([1, 1, 1], [2, 2, 2]),
        ([1, 1, 2], [2, 2, 3]),
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]),
    ],
)
def test_modify_list(v: List[int], ref: List[int]) -> None:
    assert DsList.modify_list(v) == ref


def test_benchmark_modify_list(benchmark) -> None:
    benchmark(DsList.modify_list, [1, 2, 3, 4, 5])


@pytest.mark.parametrize(
    "v, search_value, ref",
    [
        ([1, 2, 3, 4, 5], 1, [0]),
        ([1, 2, 3, 4, 5], 2, [1]),
        ([1, 2, 3, 4, 5], 9, []),
    ],
)
def test_search_list(v: List[int], search_value: int, ref: List[int]) -> None:
    assert DsList.search_list(v, search_value) == ref


def test_benchmark_search_list(benchmark) -> None:
    benchmark(DsList.search_list, [1, 2, 3, 4, 5], 2)


@pytest.mark.parametrize(
    "v, ref",
    [
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 3, 2, 2, 4, 3, 0, 5], [0, 2, 2, 3, 3, 3, 4, 5]),
    ],
)
def test_sort_list(v: List[int], ref: List[int]) -> None:
    assert DsList.sort_list(v) == ref


def test_benchmark_sort_list(benchmark) -> None:
    benchmark(DsList.sort_list, [5, 4, 3, 2, 1])


@pytest.mark.parametrize(
    "v, ref",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 3, 2, 0], [0, 2, 3, 1]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ],
)
def test_reverse_list(v: List[int], ref: List[int]) -> None:
    assert DsList.reverse_list(v) == ref


def test_benchmark_reverse_list(benchmark) -> None:
    benchmark(DsList.reverse_list, [1, 2, 3, 4, 5])


@pytest.mark.parametrize(
    "v, n, ref",
    [
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5, 1]),
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 6, [2, 3, 4, 5, 1]),
        ([1, 2, 3, 4, 5], 7, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], 10, [1, 2, 3, 4, 5]),
        ([], 0, []),
        ([], 5, []),
        ([1], 0, [1]),
        ([1], 1, [1]),
        ([1], 5, [1]),
    ],
)
def test_rotate_list(v: List[int], n: int, ref: List[int]) -> None:
    """Test rotate_list with various rotation amounts including edge cases.
    
    This test verifies that the function correctly handles:
    - Normal rotations (0 < n < len(v))
    - Rotation by length (n == len(v))
    - Rotation by more than length (n > len(v))
    - Empty lists
    - Single-element lists
    """
    assert DsList.rotate_list(v, n) == ref


def test_benchmark_rotate_list(benchmark) -> None:
    benchmark(DsList.rotate_list, [1, 2, 3, 4, 5], 2)
