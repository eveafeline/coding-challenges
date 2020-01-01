"""
Is Unique:
Implement an algorithm to determin if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_unique(s):
    cache = {}
    for c in s:
        if c in cache:
            return False
        else:
            cache[c] = True
    return True


def is_unique_str_only(s):
    return True


def check_true(l):
    for s in l:
        assert is_unique(s) is True


def check_false(l):
    for s in l:
        assert is_unique(s) is False


def test_run():
    l_True = [("abcd1234"), ("s4fad"), (""), ("@#$^%&!23456")]
    l_False = [("23ds2"), ("hb 627jh=j ()"), ("@#$^%&!$23456")]

    check_true(l_True)
    check_false(l_False)
