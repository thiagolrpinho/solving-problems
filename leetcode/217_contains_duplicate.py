'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1, 2, 3, 1]
Output: true
Example 2:

Input: [1, 2, 3, 4]
Output: false
Example 3:

Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
'''
import pytest
from typing import List
from collections import Counter

@pytest.mark.parametrize('input_and_output', [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
    ])
def test_contains_duplicate(input_and_output):
    input_list = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = containsDuplicate(input_list)
    assert expected_output == predicted_output


def containsDuplicate(nums: List[int]) -> bool:
    digits_count = dict()
    for digit in nums:
        if digit in digits_count:
            return True
        else:
            digits_count[digit] = 1
    return False
