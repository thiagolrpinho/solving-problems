'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
'''
import pytest
from typing import List  # Need to import this so we can use List[int] in args


@pytest.mark.parametrize('input_and_output', [
    (([4, 2, 3]), True),
    (([4, 2, 1]), False),
    (([2, 5, 4, 3]), False),
    (([3, 4, 2, 3]), False),
    (([1, 1, 1]), True),
    (([1, 0, 3, 4]), True)])
def test_check_possibility(input_and_output):
    input_list = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = checkPossibility(input_list)

    assert predicted_output == expected_output


def checkPossibility(nums: List[int]) -> bool:
    if len(nums) < 3:
        return True
    descrecement_count = 2
    for i, _ in enumerate(nums[:-1]):
        if nums[i] > nums[i+1]:
            descrecement_count -= 1
            if i == 0:
                nums[i] = nums[i+1]
            else:
                if nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
        if descrecement_count == 0:
            return False
    return True
