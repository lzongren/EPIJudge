import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    if not A or pivot_index < 0 or pivot_index >= len(A):
        return

    pivot_value = A[pivot_index]

    # A[:less] represents less than pivot value
    less = 0
    # A[index:greater] represents un-processed elements
    index = 0
    # A[greater:] represents greater than pivot value
    greater = len(A)

    while index < greater:
        if A[index] < pivot_value:
            A[less], A[index] = A[index], A[less]
            less += 1
            index += 1
        elif A[index] == pivot_value:
            index += 1
        else:
            greater -= 1
            A[index], A[greater] = A[greater], A[index]


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
