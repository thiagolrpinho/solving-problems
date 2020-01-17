'''
Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

import pytest
from collections import Counter

@pytest.mark.parametrize('input_and_output', [
    ("tree", "eetr"),
    ("cccaaa", "cccaaa"),
    ("Aabb", "bbAa")])
def test_frequency_sort(input_and_output):
    input_string = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = frequencySort(input_string)
    assert expected_output == predicted_output


def frequencySort(s: str) -> int:
    letters_count = Counter(s)
    sorted_string = ""
    for letter, times in letters_count.most_common():
        for _ in range(times):
            sorted_string += letter

    return sorted_string
