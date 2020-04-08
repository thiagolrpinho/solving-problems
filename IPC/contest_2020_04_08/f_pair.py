"""
Problem Statement
Problem Statement
Find the number of ways to choose a pair of an even number and an odd number from the positive integers between 
1
 and 
K
 (inclusive). The order does not matter.

Constraints
2
≤
K
≤
100
K
 is an integer.
Input
Input is given from Standard Input in the following format:

K

Output
Print the number of ways to choose a pair of an even number and an odd number from the positive integers between 
1
 and 
K
 (inclusive).

Sample Input 1
3
Sample Output 1
2
Two pairs can be chosen: 
(
2
,
1
)
 and 
(
2
,
3
)
.

Sample Input 2
6
Sample Output 2
9
Sample Input 3
11
Sample Output 3
30
Sample Input 4
50
Sample Output 4
625
"""
import pytest 

@pytest.mark.parametrize('input_and_output', [
    (3, 2),
    (6, 9),
    (11, 30),
    (50, 625),
])
def test_function(input_and_output):
    first_divisible = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = function(first_divisible)
    assert expected_output == predicted_output


def function(num: int) -> int:
    if num%2 == 0:
        value = round(num/2)**2
    else:
        value = round(num/2) * (round(num/2)-1)
    return value

''' Versao V judge '''
line = input()
num = [int(n) for n in line.split()]
num = num[0]
if num%2 == 0:
    value = round(num/2)**2
else:
    value = round(num/2) * (round(num/2)-1)
print(value)