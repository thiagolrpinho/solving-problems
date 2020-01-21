'''Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both
arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your
algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is
better?
What if elements of nums2 are stored on disk, and the memory is limited such
that you cannot load all elements into the memory at once?
'''
import pytest
from typing import List
from collections import Counter

@pytest.mark.parametrize('input_and_output', [
    (([1,2,2,1], [2,2]), [2,2]),
    (([4,9,5], [9,4,9,8,4]), [4,9]),
    ])
def test_intersect(input_and_output):
    first_input_integer = input_and_output[0][0]
    second_input_integer = input_and_output[0][1]
    expected_output = input_and_output[1]
    predicted_output = intersect(first_input_integer, second_input_integer)
    assert expected_output == predicted_output


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    found_numbers = dict()
    for number in nums1:
        if number not in found_numbers:
            found_numbers[number] = [1, 0]
        else:
            found_numbers[number][0] += 1
    for number in nums2:
        if number in found_numbers:
            found_numbers[number][1] += 1
    return [key for key, val in found_numbers.items()
            for times in range(min(val))]




