'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''
import pytest 
from math import factorial
@pytest.mark.parametrize('input_and_output', [
    (3, 0),
    (5, 1)
    ])
def test_trailing_zeroes(input_and_output):
    input_integer = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = trailingZeroes(input_integer)
    assert predicted_output == expected_output

def trailingZeroes(n: int) -> int:
    if n < 0:
        return 0
    factorial_string = str(factorial(n))
    number_of_trailing_zeroes = 0
    for i in range(len(factorial_string) - 1, -1, -1):
        if factorial_string[i] == '0':
            number_of_trailing_zeroes += 1
        else:
            break
    return number_of_trailing_zeroes
