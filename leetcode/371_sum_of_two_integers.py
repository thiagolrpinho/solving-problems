'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:
371_sum_of_two_integers
Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''
import pytest

@pytest.mark.parametrize('input_and_output', [
    ([1, 2], 3),
    ([-2, 3], 1)])
def test_get_sum(input_and_output):
    first_input_integer = input_and_output[0][0]
    second_input_integer = input_and_output[0][1]
    expected_output = input_and_output[1]
    predicted_output = getSum(first_input_integer, second_input_integer)
    assert expected_output == predicted_output


def getSum(a: int, b: int) -> int:
    return sum([a, b])
