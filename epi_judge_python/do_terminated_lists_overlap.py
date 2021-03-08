import functools

import typing

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def len_listnode(node: typing.Optional[ListNode]):
        # Using recursive would cause heap size growing too much
        # if not node:
        #     return 0
        # return 1 + len_listnode(node.next)
        l = 0
        while node:
            l += 1
            node = node.next
        return l

    def find_overlapping_head(
        l0: ListNode, l1: ListNode, len0: int, len1: int
    ) -> ListNode:
        diff = len1 - len0
        for _ in range(diff):
            l1 = l1.next

        while l0 and l1:
            if l0 is l1:
                return l0
            else:
                l0 = l0.next
                l1 = l1.next

        return None

    len0 = len_listnode(l0)
    len1 = len_listnode(l1)

    return (
        find_overlapping_head(l0, l1, len0, len1)
        if len0 < len1
        else find_overlapping_head(l1, l0, len1, len0)
    )


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure("Invalid result")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "do_terminated_lists_overlap.py",
            "do_terminated_lists_overlap.tsv",
            overlapping_no_cycle_lists_wrapper,
        )
    )
