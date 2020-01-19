'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money
of each house, determine the maximum amount of money you can rob tonight
without alerting the police.

Example 1:

Input: [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and 
rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''
import pytest 
from typing import List
import heapq
@pytest.mark.parametrize('input_and_output', [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([2, 1, 1, 2], 4),
    ([1, 7, 9, 4], 11),
    ([4, 1, 2, 7, 5, 3, 1], 14)])
def test_rob(input_and_output):
    input_integer = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = rob(input_integer)
    assert predicted_output == expected_output

def rob(nums: List[int]) -> int:
    ''' Based on solution develop by prudentprogrammer '''
    previous_number = current = 0
    for num in nums:
        before_previous = previous_number
        ''' This represents the nums[i-2]th value '''
        previous_number = current
        ''' This represents the nums[i-1]th value '''
        current = max(num + before_previous, previous_number)
        ''' Here we compare if the current plus the one before previous is
            as better choice than the previous'''
    return current
