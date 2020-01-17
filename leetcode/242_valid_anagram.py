'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
import pytest
from collections import Counter

@pytest.mark.parametrize('input_and_output', [
    (["anagram", "nagaram"], True),
    (["rat", "car"], False),
    (["ab", "a"], False),
    (["aacc", "ccac"], False)
    ])
def test_is_anagram(input_and_output):
    s_input_string = input_and_output[0][0]
    t_input_string = input_and_output[0][1]
    expected_output = input_and_output[1]
    predicted_output = isAnagram(s_input_string, t_input_string)
    assert expected_output == predicted_output


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_letters_count = Counter(s)
    t_letters_count = Counter(t)
    return s_letters_count == t_letters_count
