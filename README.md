# llm-benchmarking-py

A collection of Python functions designed to benchmark LLM (Large Language Model) projects. This library provides various algorithmic and data structure implementations that can be used to evaluate and measure the performance of code generation and optimization tasks.

## Overview

This project contains a comprehensive suite of benchmarking utilities organized into different categories, including algorithms, data structures, control flow operations, string operations, and SQL queries. Each module includes both functional implementations and corresponding benchmark tests using pytest-benchmark.

## Features

The library includes the following modules:

### 🔢 Algorithms
- **Primes**: Prime number detection, prime summation, and prime factorization
- **Sort**: Various sorting algorithms including quicksort, dutch flag partition, and finding max-n elements

### 📊 Data Structures
- **DsList**: List manipulation operations including modify, search, sort, reverse, rotate, and merge

### 🔁 Control Flow
- **SingleForLoop**: Single-loop operations like sum range, max list, and sum modulus
- **DoubleForLoop**: Nested-loop operations including sum square, sum triangle, count pairs, and matrix operations

### 📝 Strings
- **StrOps**: String operations including reverse and palindrome checking

### 🗄️ SQL
- **SqlQuery**: Database query operations for album queries, joins, and invoice operations

### 🎲 Utilities
- **GenList**: Random list and matrix generation for testing purposes

## Prerequisites

- Python 3.8 or higher
- Poetry (Python dependency management tool)

## Installation

Install the project dependencies using Poetry:

```shell
poetry install
```

## Usage

### Running the Demo

Execute the main demo script to see examples of all available functions:

```shell
poetry run main
```

### Using as a Library

Import and use individual modules in your code:

```python
from llm_benchmark.datastructures.dslist import DsList
from llm_benchmark.algorithms.primes import Primes
from llm_benchmark.strings.strops import StrOps

# Example: List operations
test_list = [1, 2, 3, 4, 5]
rotated = DsList.rotate_list(test_list, 2)  # [3, 4, 5, 1, 2]
reversed_list = DsList.reverse_list(test_list)  # [5, 4, 3, 2, 1]

# Example: Prime operations
is_prime = Primes.is_prime_ineff(17)  # True
prime_sum = Primes.sum_primes(10)  # Sum of primes up to 10

# Example: String operations
is_palindrome = StrOps.palindrome("racecar")  # True
reversed_str = StrOps.str_reverse("hello")  # "olleh"
```

## Testing

### Run Unit Tests

Execute all unit tests without benchmarks:

```shell
poetry run pytest --benchmark-skip tests/
```

### Run Benchmarks

Execute performance benchmarks:

```shell
poetry run pytest --benchmark-only tests/
```

### Run All Tests

Run both unit tests and benchmarks:

```shell
poetry run pytest tests/
```

## Project Structure

```
llm-benchmarking-py/
├── src/
│   └── llm_benchmark/
│       ├── algorithms/       # Algorithm implementations
│       ├── control/          # Control flow operations
│       ├── datastructures/   # Data structure operations
│       ├── generator/        # Test data generators
│       ├── sql/              # SQL query operations
│       └── strings/          # String manipulation
├── tests/                    # Unit tests and benchmarks
├── data/                     # Data files (e.g., SQL databases)
├── main.py                   # Demo script
├── pyproject.toml            # Project dependencies
└── README.md                 # This file
```

## Development

This project uses:
- **pytest** for testing
- **pytest-benchmark** for performance benchmarking
- **black** for code formatting
- **isort** for import sorting

## Contributing

When adding new functions:
1. Implement the function in the appropriate module
2. Add corresponding unit tests in the `tests/` directory
3. Include benchmark tests for performance measurement
4. Ensure all tests pass before submitting

## License

This project is maintained by TurinTech AI.
