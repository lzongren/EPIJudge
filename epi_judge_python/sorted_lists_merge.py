from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    if not L1:
        return L2
    if not L2:
        return L1

    h = None
    t = None

    while L1 and L2:
        if L1.data < L2.data:
            if not h:
                h = L1
                t = L1
            else:
                t.next = L1
                t = t.next
            L1 = L1.next
        else:
            if not h:
                h = L2
                t = L2
            else:
                t.next = L2
                t = t.next
            L2 = L2.next

    while L1:
        t.next = L1
        t = t.next
        L1 = L1.next
    while L2:
        t.next = L2
        t = t.next
        L2 = L2.next

    return h


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
