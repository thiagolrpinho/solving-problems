'''
mplement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().
'''

import pytest 

@pytest.mark.parametrize('input_and_output', [
    (["hello", "ll"], 2),
    (["aaaaa", "bba"], -1),
    (["", ""], 0)
    ])
def test_str_str(input_and_output):
    s_input_string = input_and_output[0][0]
    t_input_string = input_and_output[0][1]
    expected_output = input_and_output[1]
    predicted_output = strStr(s_input_string, t_input_string)
    assert expected_output == predicted_output

def strStr(haystack: str, needle: str) -> int:
    if not needle or needle not in haystack:
        return -1
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i