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


def longestCommonPrefix(list_of_strings: List[str]) -> str:
    ''' if we imagine a list of strings as a matrix of characters.
        Then each string can be interpred as a line and each letter
        position as a column'''
    if not list_of_strings:
        return ""
    smallest_length = len(list_of_strings[0])
    for string in list_of_strings:
        if len(string) < smallest_length:
            smallest_length = len(string)
    horizontal_index = 0
    while horizontal_index < smallest_length:
        character = list_of_strings[0][horizontal_index]
        vertical_index = 1
        while vertical_index < len(list_of_strings):
            if list_of_strings[vertical_index][horizontal_index] != character:
                return list_of_strings[0][:horizontal_index]
            vertical_index += 1
        horizontal_index += 1
    return list_of_strings[0][:horizontal_index]
