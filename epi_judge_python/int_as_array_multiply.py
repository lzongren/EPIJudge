from typing import List

from test_framework import generic_test

# 986
#  25
# ___
#  30
# 16


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    if not num1:
        return num2
    if not num2:
        return num1

    sign = -1 if ((num1[0] < 0) ^ (num2[0] < 0)) else 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    result = [0] * (len(num1) + len(num2))

    for j in reversed(range(len(num2))):
        for i in reversed(range(len(num1))):
            k = i + j + 1

            result[k] += num1[i] * num2[j]
            result[k - 1] += result[k] // 10
            result[k] = result[k] % 10

    k = 0
    while k < len(result) and result[k] == 0:
        k += 1
    result = result[k:]

    if result:
        result[0] = result[0] * sign
        return result
    else:
        return [0]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
