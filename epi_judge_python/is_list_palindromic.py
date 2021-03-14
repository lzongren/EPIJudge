from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L or L.next is None:
        return True

    m = L

    def is_palindrome_recursive_internal(n: ListNode) -> bool:
        """
        Bottom-up approach to test palindromic.
        Args:
            n: bottom-up pointer moving along the list.
        """
        nonlocal m
        if n.next is None:
            return m.data == n.data

        rest_palindrome = is_palindrome_recursive_internal(n.next)
        m = m.next

        return rest_palindrome and m.data == n.data

    def is_palindrome_split_internal(l: ListNode) -> bool:
        # split list
        h = l
        n = l
        while h and h.next:
            h = h.next.next
            n = n.next

        # reverse 2nd half
        reverse_h = None
        while n:
            nachste = n.next
            n.next = None
            if not reverse_h:
                reverse_h = n
            else:
                n.next = reverse_h
                reverse_h = n
            n = nachste

        h = l
        while h and reverse_h:
            if h.data != reverse_h.data:
                return False
            h = h.next
            reverse_h = reverse_h.next
        return True

    return is_palindrome_split_internal(L)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_list_palindromic.py",
            "is_list_palindromic.tsv",
            is_linked_list_a_palindrome,
        )
    )
