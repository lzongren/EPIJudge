import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    if not l or not l.next:
        return l

    l_h = None
    l_t = None
    e_h = None
    e_t = None
    g_h = None
    g_t = None

    i = l
    while i:
        nachste = i.next
        i.next = None

        if i.data < x:
            if not l_h:
                l_h = i
                l_t = i
            else:
                l_t.next = i
                l_t = i
        elif i.data == x:
            if not e_h:
                e_h = i
                e_t = i
            else:
                e_t.next = i
                e_t = i
        else:
            if not g_h:
                g_h = i
                g_t = i
            else:
                g_t.next = i
                g_t = i
        i = nachste

    dummy = ListNode(0)
    h = dummy
    t = dummy
    if l_h:
        t.next = l_h
        t = l_t
    if e_h:
        t.next = e_h
        t = e_t
    if g_h:
        t.next = g_h
        t = g_t

    return h.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
