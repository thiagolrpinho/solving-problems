'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum
of the squares of its digits, and repeat the process until the
number equals 1 (where it will stay), or it loops endlessly in a
cycle which does not include 1. Those numbers for which this process
ends in 1 are happy numbers.
Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
import pytest


@pytest.mark.parametrize('input_and_output', [
    (19, True)
    ])
def test_is_happy(input_and_output):
    input_integer = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = isHappy(input_integer)
    assert predicted_output == expected_output

def isHappy(n: int) -> bool:
    return False

