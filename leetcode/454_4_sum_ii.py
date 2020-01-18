'''
Medium

889

66

Add to List

Share
Given four lists A, B, C, D of integer values, compute how many tuples
(i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N
where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1
 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''
import pytest
from typing import List # Need to import this so we can use List[int] in args
from collections import Counter
@pytest.mark.parametrize('input_and_output', [
    (([1, 2], [-2, -1], [-1, 2], [0, 2]), 2),
    (([-1, -1], [-1, 1], [-1, 1], [1, -1]), 6)
    ])
def test_three_sum(input_and_output):
    first_input_list = input_and_output[0][0]
    second_input_list = input_and_output[0][1]
    third_input_list = input_and_output[0][2]
    fourth_input_list = input_and_output[0][3]

    expected_output = input_and_output[1]
    predicted_output = fourSumCount(
        first_input_list, second_input_list,
        third_input_list, fourth_input_list)
    assert predicted_output == expected_output


def fourSumCount(
        A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    AB = Counter([a+b for a in A for b in B])
    return sum(AB[-c-d] for c in C for d in D)


