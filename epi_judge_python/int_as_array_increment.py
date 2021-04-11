from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    if not A:
        return [1]

    acc = 1
    for i in reversed(range(len(A))):
        sum = acc + A[i]
        A[i] = sum % 10
        acc = sum // 10

    if acc > 0:
        A.insert(0, acc)
    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_increment.py", "int_as_array_increment.tsv", plus_one
        )
    )
