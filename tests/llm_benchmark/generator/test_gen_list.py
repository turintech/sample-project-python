import pytest

from llm_benchmark.generator.gen_list import GenList


def test_random_matrix_dimensions():
    """Test that random_matrix creates a matrix with correct dimensions (n rows, m columns)."""
    # Test case 1: 3 rows, 5 columns
    n, m = 3, 5
    matrix = GenList.random_matrix(n, m)
    
    assert len(matrix) == n, f"Expected {n} rows, got {len(matrix)}"
    for i, row in enumerate(matrix):
        assert len(row) == m, f"Expected {m} columns in row {i}, got {len(row)}"
    
    # Test case 2: 2 rows, 4 columns
    n, m = 2, 4
    matrix = GenList.random_matrix(n, m)
    
    assert len(matrix) == n, f"Expected {n} rows, got {len(matrix)}"
    for i, row in enumerate(matrix):
        assert len(row) == m, f"Expected {m} columns in row {i}, got {len(row)}"
    
    # Test case 3: 4 rows, 2 columns
    n, m = 4, 2
    matrix = GenList.random_matrix(n, m)
    
    assert len(matrix) == n, f"Expected {n} rows, got {len(matrix)}"
    for i, row in enumerate(matrix):
        assert len(row) == m, f"Expected {m} columns in row {i}, got {len(row)}"


def test_random_list_length():
    """Test that random_list creates a list with correct length."""
    n = 10
    m = 100
    lst = GenList.random_list(n, m)
    
    assert len(lst) == n, f"Expected list of length {n}, got {len(lst)}"
