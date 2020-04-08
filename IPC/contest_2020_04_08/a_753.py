"""
Problem Statement
Shichi-Go-San (literally "Seven-Five-Three") is a traditional event in a certain country to celebrate the growth of seven-, five- and three-year-old children.

Takahashi is now 
X
 years old. Will his growth be celebrated in Shichi-Go-San this time?

Constraints
1
≤
X
≤
9
X
 is an integer.
Input
Input is given from Standard Input in the following format:

X

Output
If Takahashi's growth will be celebrated, print YES; if it will not, print NO.

Sample Input 1
5
Sample Output 1
YES
The growth of a five-year-old child will be celebrated.

Sample Input 2
6
Sample Output 2
NO
See you next year.
"""
import pytest 

@pytest.mark.parametrize('input_and_output', [
    (5, "YES"),
    (6,"NO"),
])
def test_function(input_and_output):
    first_divisible = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = function(first_divisible)
    assert expected_output == predicted_output


def function(num: int) -> int:
    predicted_value = "NO"
    if num in [3, 5, 7]:
        predicted_value = "YES"
    return predicted_value

''' Versao V judge'''
line = input()
num = [int(n) for n in line.split()][0]
predicted_value = "NO"
if num in [3, 5, 7]:
    predicted_value = "YES"
print(predicted_value)