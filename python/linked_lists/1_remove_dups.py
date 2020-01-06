"""
Remove Dups:
Write code to remove duplicates from an unsorted linked list.

How would you solve this problem if a temporary buffer is not allowed?

# 9, #40
"""
from collections import namedtuple

from linked_list import LinkedList

Case = namedtuple("Case", ["test_list", "expected"])


def method(ll: LinkedList) -> None:
    cur = ll.head
    cache = {cur.data}
    while cur.next:
        if cur.next.data in cache:
            print('cur.next.data in cache', cur.next.data)
            cur.next = cur.next.next
        else:
            cache.add(cur.next.data)
            cur = cur.next


def test_run():
    test_cases = [Case(LinkedList.from_list([1, 2, 3, 4, 2, 5]), [1, 2, 3, 4, 5]),
                  Case(LinkedList.from_list(['spam', 'egg', 'ham', 'spam']), [
                       'spam', 'egg', 'ham']),
                  Case(LinkedList.from_list(['spam', 'egg', 'ham', 'ham']),
                       ['spam', 'egg', 'ham']),
                  Case(LinkedList.from_list(['spam', 'spam', 'egg', 'egg', 'ham', 'ham']),
                       ['spam', 'egg', 'ham'])]
    for case in test_cases:
        method(case.test_list)
        assert case.test_list.to_list() == case.expected
