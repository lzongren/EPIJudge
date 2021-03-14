from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:

    is_even = True
    i = L

    even_h = None
    even_t = None

    odd_h = None
    odd_t = None

    while i:
        nachste = i.next
        i.next = None

        if is_even:
            if even_h is None:
               even_h = i
               even_t = i
            else:
                even_t.next = i
                even_t = even_t.next
        else:
            if odd_h is None:
                odd_h = i
                odd_t = i
            else:
                odd_t.next = i
                odd_t = odd_t.next
        is_even = not is_even
        i = nachste

    if not even_h:
        return odd_h

    even_t.next = odd_h
    return even_h


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
