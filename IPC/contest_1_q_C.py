""" C - Happy Birthday! Problem Statement E869120's and square1001's 
16 -th birthday is coming soon. Takahashi from AtCoder Kingdom gave them
a round cake cut into  16  equal fan-shaped pieces.  E869120 and
square1001 were just about to eat  A  and  B  of those pieces,
respectively, when they found a note attached to the cake saying that
"the same person should not take two adjacent pieces of cake".  Can both
of them obey the instruction in the note and take desired numbers of pieces
of cake?  Constraints A  and  B  are integers between  1  and  16(inclusive).
A + B  is at most  16 . 
Input
Input is given from Standard Input in the
following format:  A   B
Output If both E869120 and square1001 can obey
the instruction in the note and take desired numbers of pieces of cake,
print Yay!; otherwise, print :(.  
Sample  Input 1
5 4 
Sample  Output 1
Yay! Both of them can take desired number of pieces as follows:    
Sample  Input 2
8 8 
Sample  Output 2
Yay! Both of them can take desired number of pieces as follows:    
Sample  Input 3
11 4 
Sample  Output 3
:( In this case, there is no way for them to take desired
number of pieces, unfortunately.
"""
import pytest

@pytest.mark.parametrize('input_and_output', [
    (5, 4, "Yay!"),
    ( 8, 8, "Yay!"),
    ( 11, 4, ":(")])
def test_cake_adjacency(input_and_output):
    input_a = input_and_output[0]
    input_b = input_and_output[1]
    expected_output = input_and_output[2]
    predicted_output = cake_adjacency(input_a, input_b)
    assert expected_output == predicted_output


def cake_adjacency(num_a: int, num_b: int) -> int:
    is_it_possible = "Yay!"
    if num_a > 8 or num_b > 8:
        is_it_possible = ":("
    return is_it_possible

''' Versao V judge'''
line = input()
num_a, num_b = [int(n) for n in line.split()]
is_it_possible = "Yay!"
if num_a > 8 or num_b > 8:
    is_it_possible = ":("
print(is_it_possible)