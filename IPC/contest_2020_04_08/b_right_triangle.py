"""
Problem Statement
There is a right triangle 
A  B  C   with   ∠  A  B  C  =  90  °
.

Given the lengths of the three sides, 
|
A
B
|
,
|
B
C
|
 and 
|
C
A
|
, find the area of the right triangle 
A
B
C
.

It is guaranteed that the area of the triangle 
A
B
C
 is an integer.

Constraints
1
≤
|
A
B
|
,
|
B
C
|
,
|
C
A
|
≤
100
All values in input are integers.
The area of the triangle 
A
B
C
 is an integer.
Input
Input is given from Standard Input in the following format:

|
A
B
|
 
|
B
C
|
 
|
C
A
|

Output
Print the area of the triangle 
A
B
C
.

Sample Input 1
3 4 5
Sample Output 1
6
tri

This triangle has an area of 
6
.

Sample Input 2
5 12 13
Sample Output 2
30
This triangle has an area of 
30
.

Sample Input 3
45 28 53
Sample Output 3
630
This triangle has an area of 
630
.
"""
import pytest

@pytest.mark.parametrize('input_and_output', [
    (3, 4, 5, 6),
    (5, 12, 13, 30),
    (45, 28, 54, 630)])
def test_function(input_and_output):
    num_a = input_and_output[0]
    num_b = input_and_output[1]
    num_c = input_and_output[2]
    expected_output = input_and_output[3]
    
    predicted_output = function(num_a, num_b, num_c)
    assert expected_output == predicted_output


def function(num_a, num_b, num_c):
    sides = [num_a, num_b, num_c]
    sides.sort()
    area = round(sides[0] * sides[1]/2)
    return area

line = input()
sides= [int(n) for n in line.split()]
sides.sort()
area = round(sides[0] * sides[1]/2)
print(area)