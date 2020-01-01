"""
implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string.

You can assume the string has only uppercase and lowercase letters (a-z).
"""
from collections import namedtuple

Case = namedtuple('Case', ['test_string', 'expected'])


def string_compression(s):
    # initialize cache variables
    result = ""
    count = 1
    prev = s[0]
    # for character in string[1:]
    # if character is not the same as prev
    # result += prev + str(count) if count > 1 else prev
    # count = 1 and prev = character
    # if character is same as prev
    # count += 1 and prev = character
    # increase character count
    # if character is None, result += prev + c_count
    for i, c in enumerate(s[1:], 1):
        if i == len(s) - 1:
            if c != prev:
                result += prev + str(count) + c if count > 1 else prev + c
            else:
                result += prev + str(count + 1)
        else:
            if c != prev:
                result += prev + str(count) if count > 1 else prev
                count = 1
                prev = c
            else:
                count += 1
                prev = c
    return result


def string_compression_iter(s):
    # use itertools.groupby
    pass


def test_run():
    test_cases = (Case("aabcccccaaa", "a2bc5a3"),
                  Case("abcd", "abcd"), Case("AAaabCCCcccccDd", "A2a2bC3c5Dd"))

    for case in test_cases:
        result = string_compression(case.test_string)
        assert result == case.expected
