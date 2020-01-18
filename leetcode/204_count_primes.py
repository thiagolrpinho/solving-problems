'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
import pytest

@pytest.mark.parametrize('input_and_output', [
    (10, 4),
    (5, 2),
    (3, 1),
    (6, 3),
    (8, 4)])
def test_count_primes(input_and_output):
    input_natural = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = countPrimes(input_natural)
    assert expected_output == predicted_output


def countPrimes(n: int) -> int:
    return False