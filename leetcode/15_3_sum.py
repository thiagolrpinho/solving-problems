'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
import pytest
from typing import List # Need to import this so we can use List[int] in args

@pytest.mark.parametrize('input_and_output', [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 0, 0, 0], [[0, 0, 0]])
    ])
def test_three_sum(input_and_output):
    input_list = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = threeSum(input_list)
    assert predicted_output == expected_output

def threeSum(numbers: List[int]) -> List[List[int]]:
    target = 0
    numbers.sort()
    numbers_size = len(numbers)
    triplets_sum = set()
    for anchor_index, anchor_number in enumerate(numbers[0:-2]):
        if anchor_index > 0 and numbers[anchor_index-1] == anchor_number:
            ''' If it's the same anchor as before. The triplets would be
                the same '''
            continue
        bottom_index, top_index = anchor_index+1, numbers_size-1

        summation = anchor_number + numbers[bottom_index]\
            + numbers[bottom_index+1]
        ''' First we try the smaller possible sum for this anchor '''
        if summation > target:
            ''' If it's already above the target, then there's nothing
                else to search for this anchor'''
            break
        else:
            summation = anchor_number + numbers[top_index] + numbers[top_index-1]
            ''' Then we try the greater possible sum for this anchor '''
            if summation < target:
                ''' If it's smaller than the target, then there's
                    nothing else to search for this anchor
                '''
                continue
            else:
                ''' If those conditions are not true
                    then there's still something to find '''
                while(bottom_index < top_index):
                    summation = anchor_number + numbers[bottom_index]\
                        + numbers[top_index]
                    if summation > target:
                        top_index -= 1
                    elif summation < target:
                        bottom_index += 1
                    else:
                        triplets_sum.add((
                            anchor_number, numbers[bottom_index],
                            numbers[top_index]))
                        bottom_index += 1
    return list(map(lambda x: list(x), triplets_sum))