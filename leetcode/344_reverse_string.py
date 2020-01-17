'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
import pytest
from typing import List

@pytest.mark.parametrize('input_and_output', [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])])
def test_reverse_string(input_and_output):
    input_list_string = input_and_output[0]
    expected_output = input_and_output[1]
    reverse_string(input_list_string)
    assert expected_output == input_list_string

def reverse_string(s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead
        """
        s.reverse()
