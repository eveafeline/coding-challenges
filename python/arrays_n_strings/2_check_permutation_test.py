"""
Given two strings, write a method to decide if one is a permutation of the other.

"""


def check_permutation(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    return l1 == l2


def check_true(l):
    for s in l:
        assert check_permutation(s[0], s[1]) is True


def check_false(l):
    for s in l:
        assert check_permutation(s[0], s[1]) is False


def test_run():
    l_True = [("abcd", "acbd"), ("test", "tset"),
              ("abcd", "abcd"), ("geeksforgeeks", "forgeeksgeeks")]
    l_False = [("test", "ttew")]

    check_true(l_True)
    check_false(l_False)
