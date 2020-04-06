"""B - Add Sub Mul Problem Statement You are given two integers  A and  B .
Find the largest value among  A + B ,  A − B  and  A × B . 
Constraints − 1000 ≤ A , B ≤ 1000 All values in input are integers.
Input Input is given from Standard Input in the following
format:  A   B  Output Print the largest value among 
A + B ,  A − B  and  A × B . 
Sample Input 1
3 1
Sample Output 1
4 3 + 1 = 4 ,  3 − 1 = 2  and  3 × 1 = 3 .
The largest among them is  4 . 
Sample Input 2
4 -2
Sample Output 2
6 The largest is  4 − ( − 2 ) = 6 . 
Sample Input 3
0 0
Sample Output 3
0"""
import pytest

@pytest.mark.parametrize('input_and_output', [
    (3, 1, 4),
    (4, -2, 6),
    (0, 0, 0)])
def test_smaller_divisible_number(input_and_output):
    input_a = input_and_output[0]
    input_b = input_and_output[1]
    expected_output = input_and_output[2]
    predicted_output = greater_sum_div_mul(input_a, input_b)
    assert expected_output == predicted_output


def greater_sum_div_mul(num_a: int, num_b: int) -> int:
    return False