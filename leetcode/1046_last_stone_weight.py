'''
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 
'''
import pytest
from typing import List

@pytest.mark.parametrize('input_and_output', [
    ([2, 7, 4, 1, 8, 1], 1), ([1, 2, 3], 0)])
def test_last_stone_weight(input_and_output):
    input_list = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = lastStoneWeight(input_list)
    assert expected_output == predicted_output


def lastStoneWeight(stones: List[int]) -> int:
    while(len(stones) > 1):
        stones.sort()
        heaviest_stone = stones.pop()
        other_stone = stones.pop()
        result_stone = heaviest_stone - other_stone
        if result_stone is not 0:
            stones.append(result_stone)
    if stones:
        return stones[0]
    else:
        return 0
