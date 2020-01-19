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
    ([1, 7, 9, 4], 11)])
def test_rob(input_and_output):
    input_integer = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = rob(input_integer)
    assert predicted_output == expected_output

def rob(nums: List[int]) -> int:
    ''' First we calculate the profit
        of each index as it's value
        subtracted by the value of
        not choosing it's neigbours'''
    heap_profits = [(a[1]+a[2]-a[0], i) for i, a in enumerate(zip(
        nums, nums[1:]+[0], [0]+nums[:-1]))]
    ''' As we'll be working with a min-heap, we multiplied
        the profit by minus 1 so the better profit is choosen first
    '''
    heapq.heapify(heap_profits)
    final_value = 0
    choosen_index = set()
    while heap_profits:
        ''' Now we have to pop the smaller element of the heap '''
        profit, index = heapq.heappop(heap_profits)
        if index+1 in choosen_index or index-1 in choosen_index:
            continue
        ''' If it's not an option already blocked by other choices,
            we then add then as one choice '''
        choosen_index.add(index)
        final_value += nums[index]
    return final_value
