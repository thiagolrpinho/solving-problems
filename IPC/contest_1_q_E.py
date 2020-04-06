""" E - Maximum Sum
Problem Statement
There are three positive integers A , B and C written on a blackboard. E869120 performs
the following operation K times:
Choose one integer written on the blackboard and let the chosen integer be n .
Replace the chosen integer with 2 n . What is the largest possible sum of the
integers written on the blackboard after K operations?
Constraints A , B and C
are integers between 1 and 50 (inclusive). K is an integer between 1 and 10
(inclusive). 
Input
Input is given from Standard Input in the following format:
A B C K
Output
Print the largest possible sum of the integers written on the
blackboard after K operations by E869220. 
Sample Input 1
5 3 11 1 
Sample Output 1
30 In this Sample, 5 , 3 , 11 are initially written on the blackboard, and
E869120 can perform the operation once. There are three choices: Double 5 : The
integers written on the board after the operation are 10 , 3 , 11 . Double 3 :
The integers written on the board after the operation are 5 , 6 , 11 . Double 11
: The integers written on the board after the operation are 5 , 3 , 22 . If he
chooses 3., the sum of the integers written on the board afterwards is 5 + 3 +
22 = 30 , which is the largest among 1. through 3. 
Sample Input 2
3 3 4 2 
Sample Output 2
22 E869120 can perform the operation twice. The sum of the integers
eventually written on the blackboard is maximized as follows: First, double 4 .
The integers written on the board are now 3 , 3 , 8 . Next, double 8 . The
integers written on the board are now 3 , 3 , 16 . Then, the sum of the integers
eventually written on the blackboard is 3 + 3 + 16 = 22 .
"""
import pytest

@pytest.mark.parametrize('input_and_output', [
    (5, 3, 11, 1, 30),
    (3, 3, 4, 2, 22)])
def test_maximum_sum(input_and_output):
    input_a = input_and_output[0]
    input_b = input_and_output[1]
    input_c = input_and_output[2]
    input_d = input_and_output[3]
    expected_output = input_and_output[4]
    predicted_output = maximum_sum(input_a, input_b, input_c, input_d)
    assert expected_output == predicted_output


def maximum_sum(num_a: int, num_b: int, num_c: int, num_k: int) -> int:
    numbers = [num_a, num_b, num_c]
    numbers.sort(reverse=True)
    numbers[0] *= 2**num_k
    return sum(numbers)
