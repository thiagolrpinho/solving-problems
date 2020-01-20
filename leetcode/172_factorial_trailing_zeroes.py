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

@pytest.mark.parametrize('input_and_output', [
    (3, 0),
    (5, 1),
    (10, 2)
    ])
def test_trailing_zeroes(input_and_output):
    input_integer = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = trailingZeroes(input_integer)
    assert predicted_output == expected_output

def trailingZeroes(n: int) -> int:
    '''The number of trailling zeros
        if affected by primes five and two in the factorial.
        As the quantity of the two number are always equal
        or greater than the quantity fives we can use just
        the fives and it's potencies to solve it
    '''
    division_factor = 5
    number_of_trailing_zeroes = 0
    while(n/division_factor >= 1):
        number_of_trailing_zeroes += int(n/division_factor)
        division_factor *= 5
    return number_of_trailing_zeroes
