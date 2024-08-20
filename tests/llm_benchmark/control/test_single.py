from typing import List

import pytest

from llm_benchmark.control.single import SingleForLoop


@pytest.mark.parametrize("n, S", [(0, 0), (1, 0), (2, 1), (3, 3), (4, 6), (10, 45)])
def test_sum_range(n: int, S: int) -> None:
    assert SingleForLoop.sum_range(n) == S


def test_benchmark_sum_range(benchmark) -> None:
    benchmark(SingleForLoop.sum_range, 100)


@pytest.mark.parametrize(
    "v, M",
    [([0], 0), ([1, 2, 3, 4, 5], 5), ([1, 1, 1, 1, 0], 1), ([-1, -1, -1, -1, 0], 0)],
)
def test_max_list(v: List[int], M: int) -> None:
    assert SingleForLoop.max_list(v) == M


def test_benchmark_max_list(benchmark) -> None:
    benchmark(SingleForLoop.max_list, [1, 2, 3, 4, 5])


@pytest.mark.parametrize(
    "n, m, S",
    [
        (0, 2, 0),
        (1, 2, 0),
        (2, 2, 0),
        (3, 2, 2),
        (4, 2, 2),
        (10, 2, 20),
        (10, 3, 18),
        (10, 4, 12),
    ],
)
def test_sum_modulus(n: int, m: int, S: int) -> None:
    assert SingleForLoop.sum_modulus(n, m) == S


def test_benchmark_sum_modulus(benchmark) -> None:
    benchmark(SingleForLoop.sum_modulus, 100, 2)
