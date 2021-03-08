from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L or L.next is None or k <= 0:
        return L

    length = 0
    i = L
    tail = None
    while i:
        length += 1
        if i.next is None:
            tail = i
        i = i.next

    k = k % length
    if k == 0:
        return L

    # find part one - no need to shift
    # E.g., 0 -> 1, k = 1
    i = L
    for _ in range(length - k - 1):
        i = i.next
    to_shift = i.next
    i.next = None

    # bind to head
    tail.next = L
    return to_shift


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
