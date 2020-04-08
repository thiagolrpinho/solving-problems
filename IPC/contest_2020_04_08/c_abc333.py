"""
Problem Statement
You are given integers 
A
 and 
B
, each between 
1
 and 
3
 (inclusive).

Determine if there is an integer 
C
 between 
1
 and 
3
 (inclusive) such that 
A
×
B
×
C
 is an odd number.

Constraints
All values in input are integers.
1
≤
A
,
B
≤
3
Input
Input is given from Standard Input in the following format:

A
 
B

Output
If there is an integer 
C
 between 
1
 and 
3
 that satisfies the condition, print Yes; otherwise, print No.

Sample Input 1
3 1
Sample Output 1
Yes
Let 
C
=
3
. Then, 
A
×
B
×
C
=
3
×
1
×
3
=
9
, which is an odd number.

Sample Input 2
1 2
Sample Output 2
No
Sample Input 3
2 2
Sample Output 3
No
"""
import pytest

@pytest.mark.parametrize('input_and_output', [
    (3, 1, "Yes"),
    (1, 2, "No"),
    (2, 2, "No")])
def test_function(input_and_output):
    num_a = input_and_output[0]
    num_b = input_and_output[1]
    expected_output = input_and_output[2]
    predicted_output = function(num_a, num_b)
    assert expected_output == predicted_output


def function(num_a, num_b):
    value = "Yes"
    if (num_a * num_b)%2 == 0:
        value = "No"
    return value

line = input()
num_a, num_b = [int(n) for n in line.split()]
value = "Yes"
if (num_a * num_b)%2 == 0:
    value = "No"
print(value)
