'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''
import pytest
from typing import List # Need to import this so we can use List[int] in args
@pytest.mark.parametrize('input_and_output', [(([2,7,11,15], 9), [1,2]), (([2,7,11,15], 22), [2,4]), (([0,0,3,4], 0), [1,2])])
def test_num_dup_digits_at_most_n(input_and_output):
    duplicate_count = {}
    input_list = input_and_output[0][0]
    input_target = input_and_output[0][1]
    expected_output = input_and_output[1]
    predicted_output = twoSum(input_list, input_target)

    assert predicted_output == expected_output

def twoSum(numbers: List[int], target: int) -> List[int]:
    small_number_index = 0
    big_number_index = len(numbers)-1
    while(True):
        ''' As it's garanteed it'll find a valid sum for target.
        We'll look till find something'''
        summation = numbers[small_number_index] +  numbers[big_number_index]
        if summation == target:
            return [small_number_index+1, big_number_index+1]
        elif summation > target:
            '''If it's bigger, then we have to look for a smaller number to sum'''
            big_number_index -= 1
        else:
            ''' If it's smaller then we have to look for a bigger number'''
            small_number_index += 1

