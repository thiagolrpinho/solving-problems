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
    a_set, b_set = set(A), set(B)
    c_set, d_set = set(C), set(D)
    iterations_count = 0
    tuples_found = 0
    for a_anchor in a_set:
        for b_anchor in b_set:
            for c_anchor in c_set:
                if (a_anchor + b_anchor + c_anchor) * -1 in d_set:
                    tuples_found += 1
                iterations_count += 1
    return tuples_found
