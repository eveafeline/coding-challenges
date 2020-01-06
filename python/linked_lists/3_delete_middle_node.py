"""
Implement an algorithm to delete a node in the middle (i.e., any node by the first and last node,
not necessarily the exact middle) of a singly linked list, given only access to that node.

Example
Input: the node c from the linked list a > b > c > d > e > f
Result: nothing is returned, but the new linked list looks like a > b > d > e > f

#72
"""
from collections import namedtuple

from linked_list import LinkedList

Case = namedtuple("Case", ["test_list", "data", "expected"])


def method(ll: LinkedList, data: int) -> int:
    cur = ll.head
    while cur.next:
        if cur.next.data == data:
            cur.next = cur.next.next
        elif cur.data == data:
            ll.head = cur.next
            cur = cur.next
        else:
            cur = cur.next


def test_run():
    test_cases = [Case([1, 2, 3, 4, 5], 2, [1, 3, 4, 5]),
                  Case([2, 4, 6, 8, 10, 12, 14, 16, 18], 2,
                       [4, 6, 8, 10, 12, 14, 16, 18]),
                  Case([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5])]
    for case in test_cases:
        ll = LinkedList.from_list(case.test_list)
        method(ll, case.data)
        assert ll.to_list() == case.expected
