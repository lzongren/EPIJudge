from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    if not L1:
        return L2
    if not L2:
        return L1

    dummy = ListNode(0)
    tail = dummy
    acc = 0

    while L1 or L2:
        l1_data = L1.data if L1 else 0
        l2_data = L2.data if L2 else 0

        sum = l1_data + l2_data + acc
        remaind = sum % 10
        acc = int(sum / 10)

        tail.next = ListNode(remaind)
        tail = tail.next

        if L1:
            L1 = L1.next
        if L2:
            L2 = L2.next

    if acc > 0:
        tail.next = ListNode(acc)

    return dummy.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_list_add.py", "int_as_list_add.tsv", add_two_numbers
        )
    )
