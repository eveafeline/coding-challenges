"""
Implement an algorithm to find the kth to last element of a singly linked list.

# 8, 25, 41, 67, 126
"""
from collections import namedtuple

from linked_list import LinkedList

Case = namedtuple("Case", ["test_list", "k", "expected"])


def method_1(ll: LinkedList, k: int) -> int:
    length = 0
    cur = ll.head
    while cur:
        cur = cur.next
        length += 1
    if k > length:
        return None

    cur = ll.head
    for i in range(0, length - k):
        cur = cur.next

    return cur.data


def method_2(ll: LinkedList, k: int) -> int:
    dist = 0
    main = ll.head
    ref = ll.head
    # if dist == k then main should start moving
    # should stop if either main or ref is null
    while main and ref:
        if dist != k:
            ref = ref.next
            dist += 1
        else:
            main = main.next
            ref = ref.next

    if dist != k:
        return None

    return main.data


def method_3(ll: LinkedList, k: int) -> int:
    """recursive"""
    pass


def test_run_1():
    test_cases = [Case([1, 2, 3, 4, 5], 2, 4),
                  Case([2, 4, 6, 8, 10, 12, 14, 16, 18], 1, 18),
                  Case([1, 2, 3, 4, 5], 6, None)]
    for case in test_cases:
        ll = LinkedList.from_list(case.test_list)
        result = method_1(ll, case.k)
        assert result == case.expected


def test_run_2():
    test_cases = [Case([1, 2, 3, 4, 5], 2, 4),
                  Case([2, 4, 6, 8, 10, 12, 14, 16, 18], 1, 18),
                  Case([1, 2, 3, 4, 5], 6, None)]
    for case in test_cases:
        ll = LinkedList.from_list(case.test_list)
        result = method_2(ll, case.k)
        assert result == case.expected


if __name__ == "__main__":
    ll = LinkedList.from_list([1, 2, 3, 4, 5])
    k = 7
    result = method_2(ll, k)
    print(result)
