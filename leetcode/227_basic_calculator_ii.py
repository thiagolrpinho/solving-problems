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
import ast
import operator

@pytest.mark.parametrize('input_and_output', [
    ("3+2*2", 7),
    (" 3/2 ", 1),
    (" 3+5 / 2 ", 5),
    ("42", 42)])
def test_calculate(input_and_output):
    input_string = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = calculate(input_string)
    assert expected_output == predicted_output

def calculate(s: str) -> int:
    number_stack = []
    number = ''
    last_operator = '+'
    i = 0
    length = len(s)
    while i < length:
        if s[i] == ' ':
            i += 1
            continue
        if s[i].isdigit():
            number += s[i]
            j = i + 1
            while j < length and s[j].isdigit():
                number += s[j]
                j += 1
            i = j - 1
        else:
            if last_operator == "+":
                number_stack.append(int(number))
            elif last_operator == '-':
                number_stack.append(-int(number))
            elif last_operator == '*':
                number_stack.append(int(number) * number_stack.pop())
            else:
                divisor = int(number)
                number_stack.append(int(number_stack.pop()/divisor))
            last_operator = s[i]
            number = ''
        i += 1
    if number:
        if last_operator == "+":
            number_stack.append(int(number))
        elif last_operator == '-':
            number_stack.append(-int(number))
        elif last_operator == '*':
            number_stack.append(int(number) * number_stack.pop())
        else:
            divisor = int(number)
            number_stack.append(int(number_stack.pop()/divisor))
    return sum(number_stack)
            


