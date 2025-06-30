from random import randint
from typing import List
import numpy as np


class GenList:
    @staticmethod
    def random_list(n: int, m: int) -> List[int]:

        return [randint(0, m) for _ in range(n)]

    @staticmethod
    def random_matrix(n: int, m: int) -> List[List[int]]:

        return np.random.randint(0, m, size=(n, m)).tolist()