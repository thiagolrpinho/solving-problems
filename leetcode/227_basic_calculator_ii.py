'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''
import pytest

@pytest.mark.parametrize('input_and_output', [
    ("3+2*2", 7),
    (" 3/2 ", 1),
    (" 3+5 / 2 ", 5)])
def test_calculate(input_and_output):
    input_string = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = calculate(input_string)
    assert expected_output == predicted_output


def calculate(s: str) -> int:
    return False
