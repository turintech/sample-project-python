from typing import List

import pytest

from llm_benchmark.control.double import DoubleForLoop


@pytest.mark.parametrize("n, S", [(1, 0), (2, 1), (3, 5), (10, 285)])
def test_sum_square(n: int, S: int) -> None:
    assert DoubleForLoop.sum_square(n) == S


def test_benchmark_sum_square(benchmark) -> None:
    benchmark(DoubleForLoop.sum_square, 100)


@pytest.mark.parametrize("n, S", [(1, 0), (2, 1), (3, 4), (10, 165)])
def test_sum_triangle(n: int, S: int) -> None:
    assert DoubleForLoop.sum_triangle(n) == S


def test_benchmark_sum_triangle(benchmark) -> None:
    benchmark(DoubleForLoop.sum_triangle, 100)


@pytest.mark.parametrize(
    "arr, count",
    [
        ([0], 0),
        ([1, 2, 3], 0),
        ([1, 1, 1], 0),
        ([1, 1, 2], 1),
        ([1, 1, 2, 2], 2),
    ],
)
def test_count_pairs(arr: List[int], count: int) -> None:
    assert DoubleForLoop.count_pairs(arr) == count


def test_benchmark_count_pairs(benchmark) -> None:
    benchmark(DoubleForLoop.count_pairs, [1, 1, 2, 2])


@pytest.mark.parametrize(
    "arr0, arr1, count",
    [
        ([0], [0], 1),
        ([1, 2, 3], [2, 3, 1], 0),
        ([1, 1, 1], [1, 2, 3], 1),
        ([1, 1, 2], [1, 2, 2], 2),
        ([1, 1, 2, 2], [1, 1, 2, 2], 4),
    ],
)
def test_count_duplicates(arr0: List[int], arr1: List[int], count: int) -> None:
    assert DoubleForLoop.count_duplicates(arr0, arr1) == count


def test_benchmark_count_duplicates(benchmark) -> None:
    benchmark(DoubleForLoop.count_duplicates, [1, 1, 2, 2], [1, 1, 2, 2])


@pytest.mark.parametrize(
    "matrix, S",
    [
        ([[0]], 0),
        ([[0, 1], [2, 3]], 6),
        ([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 36),
    ],
)
def test_sum_matrix(matrix: List[List[int]], S: int) -> None:
    assert DoubleForLoop.sum_matrix(matrix) == S


def test_benchmark_sum_matrix(benchmark) -> None:
    benchmark(DoubleForLoop.sum_matrix, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
