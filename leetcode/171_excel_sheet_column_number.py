'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''

import pytest

@pytest.mark.parametrize('input_and_output', [
    ("A", 1),
    ("AB", 28),
    ("ZY", 701)])
def test_title_to_number(input_and_output):
    input_string = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = titleToNumber(input_string)
    assert expected_output == predicted_output


def titleToNumber(s: str) -> int:
    start_value = 64  # A in decimal is 65, so if we subtract 64 it value is 1
    numeric_base = 26  # Every new letter is a potency of 26 by an index
    sum = 0
    for i, letter in enumerate(s[::-1]):
        sum += (ord(letter) - start_value) * numeric_base ** i
    return sum

