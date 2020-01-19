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
    (" 3+5 / 2 ", 5)])
def test_calculate(input_and_output):
    input_string = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = calculate(input_string)
    assert expected_output == predicted_output


operators = {
            ast.Add: operator.add, ast.Sub: operator.sub,
            ast.Mult: operator.mul, ast.Div: operator.truediv}


def calculate(s: str) -> int:
    # supported operators
    result = 0
    ''' Let's first search for * and / as they
        have priority. '''
    s = s.replace(' ', '')
    parsed_string = ast.parse(s, mode="eval")
    return evaluation(parsed_string.body)


def evaluation(node) -> int:
    
    if isinstance(node, ast.Num): # <number>
        return node.n
    elif isinstance(node, ast.BinOp): # <left> <operator> <right>
        return int(operators[type(node.op)](evaluation(node.left), evaluation(node.right)))
    elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(node.op)](evaluation(node.operand))
