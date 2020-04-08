'''Problem Statement
You are given a positive integer N  .
Find the minimum positive integer divisible by both   2   and   N  .
Constraints  1  ≤  N  ≤  10  9  All values in input are integers.  Input  Input is given from Standard Input in the following format:    N 
Output 
Print the minimum positive integer divisible by both   2   and   N  .
Sample Input 1  3  
Sample Output 1  6  6   is divisible by both   2   and   3  . Also, there is no positive integer less than   6 that is divisible by both  2  and  3  . Thus, the answer is  6  .    
Sample Input 2  10  
Sample Output 2  10  
Sample Input 3  999999999  
Sample Output 3  1999999998'''

import pytest

@pytest.mark.parametrize('input_and_output', [
    (3, 6),
    (10, 10),
    (999999999, 1999999998)
])
def test_smaller_divisible_number(input_and_output):
    first_divisible = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = smaller_divisible_number(first_divisible)
    assert expected_output == predicted_output


def smaller_divisible_number(num: int) -> int:
    smaller_divisible_number = num
    if num%2 != 0:
        smaller_divisible_number *= 2
    return smaller_divisible_number

''' Versao V judge'''
line = input()
num = [int(n) for n in line.split()][0]
print(num)
smaller_divisible_number = num
if num%2 != 0:
    smaller_divisible_number *= 2
print(smaller_divisible_number)