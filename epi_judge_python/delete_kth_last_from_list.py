from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    if not L or k <= 0:
        return None

    length = 0
    i = L
    while i:
        length += 1
        i = i.next

    # k > length, no need to delete
    if k > length:
        return L

    # locate the previous node of k-th last node
    dummy_root = ListNode(0, L)
    i = dummy_root
    while length > k:
        i = i.next
        length -= 1

    # delete the node
    i.next = i.next.next
    return dummy_root.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "delete_kth_last_from_list.py",
            "delete_kth_last_from_list.tsv",
            remove_kth_last,
        )
    )
