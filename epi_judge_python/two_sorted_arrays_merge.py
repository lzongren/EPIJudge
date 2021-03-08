from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    i = 0
    j = 0
    l = list()

    while i < m and j < n:
        if A[i] < B[j]:
            l.append(A[i])
            i += 1
        else:
            l.append(B[j])
            j += 1

    while i < m:
        l.append(A[i])
        i += 1
    while j < n:
        l.append(B[j])
        j += 1

    del A[:]
    A.extend(l)


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "two_sorted_arrays_merge.py",
            "two_sorted_arrays_merge.tsv",
            merge_two_sorted_arrays_wrapper,
        )
    )
