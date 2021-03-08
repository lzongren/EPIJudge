from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L

    h = None
    t = None
    i = L

    while i:
        nachste = i.next
        i.next = None

        # first node
        if h is None:
            h = i
            t = i
        else:
            i.next = None
            if t.data != i.data:
                t.next = i
                t = t.next

        i = nachste

    return h


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            "remove_duplicates_from_sorted_list.tsv",
            remove_duplicates,
        )
    )
