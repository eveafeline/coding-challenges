"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string has
sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)

e.g.
INPUT: "Mr John Smith    ", 17
OUTPUT: "Mr%20John%20Smith"
"""
from collections import namedtuple

Case = namedtuple("Case", ["test_string", "length", "expected"])


def URLify(s, n):
    trimmed = s[:n]
    return trimmed.replace(' ', '%20')


def URLify_regex(s, n):
    import re

    rex = re.sub(r'[^\w\s]', ' ', s)

    return re.sub(r'\s', '%20', rex[:n])


def test_run():
    test_cases = [
        Case("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        Case("Mr John Smith      ", 15, "Mr%20John%20Smith%20%20")]

    for case in test_cases:
        result = URLify(case.test_string, case.length)
        assert result == case.expected


def test_regex():
    test_cases = [
        Case("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        Case("Mr John Smith      ", 15, "Mr%20John%20Smith%20%20")]

    for case in test_cases:
        result = URLify_regex(case.test_string,
                              case.length)
        assert result == case.expected
