""" F - Digits Sum
Problem Statement
Takahashi has two positive integers A and B.It is known that A plus B
equals N . Find the minimum possible value of "the
sum of the digits of A " plus "the sum of the digits of B " (in base 10 ).
Constraints 2 ≤ N ≤ 10 5 N is an integer.
Input
Input is given from Standard
Input in the following format: N
Output
Print the minimum possible value of "the sum of the digits of A " plus "the sum of the digits of B ". 
Sample Input 1
15
Sample Output 1
6 When A = 2 and B = 13 , the sums of their digits are 2 and 4 ,
which minimizes the value in question. 
Sample Input 2
100000 
Sample Output 2
10
"""
import pytest

@pytest.mark.parametrize('input_and_output', [
    (15, 6),
    (10, 10)
    ])
def test_digits_sum(input_and_output):
    input_a = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = digits_sum(input_a)
    assert expected_output == predicted_output


def digits_sum(num: int) -> int:
    number_of_sums = num//2 + 1 + 1*num % 2
    smallest_sum = 100000
    for i in range(1, number_of_sums):
        first_number = i
        second_number = num-i
        summation = 0
        while first_number and summation < smallest_sum:
            summation += first_number % 10
            first_number //= 10
        while second_number and summation < smallest_sum:
            summation += second_number % 10
            second_number //= 10
        if smallest_sum > summation:
            smallest_sum = summation
    return smallest_sum

''' Versao V judge'''
line = input()
num = [int(n) for n in line.split()][0]
number_of_sums = num//2 + 1 + 1*num % 2
smallest_sum = 100000
for i in range(1, number_of_sums):
    first_number = i
    second_number = num-i
    summation = 0
    while first_number and summation < smallest_sum:
        summation += first_number % 10
        first_number //= 10
    while second_number and summation < smallest_sum:
        summation += second_number % 10
        second_number //= 10
    if smallest_sum > summation:
        smallest_sum = summation
print(smallest_sum)

