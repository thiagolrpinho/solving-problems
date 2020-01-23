'''
Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower", "flow", "flight"] Output: "fl" Example 2:

Input: ["dog", "racecar", "car"] Output: "" Explanation: There is no common
prefix among the input strings. Note:

All given inputs are in lowercase letters a-z.
'''

import pytest
from typing import List


@pytest.mark.parametrize('input_and_output', [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    ])
def test_longest_common_prefix(input_and_output):
    input_list_strings = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = longestCommonPrefix(input_list_strings)
    assert expected_output == predicted_output


def longestCommonPrefix(strs: List[str]) -> str:
    return False
