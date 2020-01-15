'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3, 2, 3]
Output: 3
Example 2:

Input: [2, 2, 1, 1, 1, 2, 2]
Output: 2
'''
import pytest
from typing import List

@pytest.mark.parametrize('input_and_output', [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([3, 3, 4], 3)
    ])
def test_move_zeroes(input_and_output):
    input_list = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = majorityElement(input_list)
    assert expected_output == predicted_output


def majorityElement(nums: List[int]) -> int:
    hash_number_count = {}
    for num in nums:
        if num in hash_number_count:
            hash_number_count[num] += 1
        else:
            hash_number_count[num] = 1
    return max(hash_number_count.keys(), key=(lambda k: hash_number_count[k]))

