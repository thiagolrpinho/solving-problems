"""
Problem Statement
Let 
S
(
n
)
 denote the sum of the digits in the decimal notation of 
n
. For example, 
S
(
101
)
=
1
+
0
+
1
=
2
.

Given an integer 
N
, determine if 
S
(
N
)
 divides 
N
.

Constraints
1
≤
N
≤
10
9
Input
Input is given from Standard Input in the following format:

N

Output
If 
S
(
N
)
 divides 
N
, print Yes; if it does not, print No.

Sample Input 1
12
Sample Output 1
Yes
In this input, 
N
=
12
. As 
S
(
12
)
=
1
+
2
=
3
, 
S
(
N
)
 divides 
N
.

Sample Input 2
101
Sample Output 2
No
As 
S
(
101
)
=
1
+
0
+
1
=
2
, 
S
(
N
)
 does not divide 
N
.

Sample Input 3
999999999
Sample Output 3
Yes
"""
import pytest 

@pytest.mark.parametrize('input_and_output', [
    (12, "Yes"),
    (101,"No"),
    (999999999, "Yes")
])
def test_function(input_and_output):
    first_divisible = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = function(first_divisible)
    assert expected_output == predicted_output


def function(num: int) -> int:
    value = "No"
    summation = 0
    original_number = num
    while num:
        summation += num % 10
        num //= 10
    if original_number%summation == 0:
        value = "Yes"
    return value

''' Versao V judge '''
line = input()
num = [int(n) for n in line.split()]
num = num[0]
value = "No"
summation = 0
original_number = num
while num:
    summation += num % 10
    num //= 10
if original_number%summation == 0:
    value = "Yes"
print(value)