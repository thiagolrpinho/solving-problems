'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

import pytest
from collections import Counter

@pytest.mark.parametrize('input_and_output', [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("", -1)])
def test_max_profit(input_and_output):
    input_string = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = firstUniqChar(input_string)
    assert expected_output == predicted_output


def firstUniqChar(s: str) -> int:
    if not s:
        return -1
    letters_counted = Counter(s)
    for i in range(len(s)):
        if letters_counted[s[i]] == 1:
            return i
    return -1
