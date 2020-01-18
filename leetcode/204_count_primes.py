'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
import pytest

@pytest.mark.parametrize('input_and_output', [
    (10, 3),
    (5, 2),
    (3, 1),
    (6, 3),
    (8, 4),
    (400, 78)])
def test_count_primes(input_and_output):
    input_natural = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = countPrimes(input_natural)
    assert expected_output == predicted_output


def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    is_prime_list = [1] * n
    is_prime_list[0] = is_prime_list[1] = 0
    for i in range(2, int(n**0.5)+1):
        if is_prime_list[i] == 1:
            is_prime_list[i * i:n:i] = [0] * len(is_prime_list[i*i:n:i])
    return sum(is_prime_list)
