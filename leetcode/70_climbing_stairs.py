'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
import pytest
from functools import lru_cache
@pytest.mark.parametrize('input_and_output', [
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (10, 89)])
def test_climb_stairs(input_and_output):
    input_list = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = climbStairs(input_list)
    assert expected_output == predicted_output


@lru_cache(None)
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairs(n-1) + climbStairs(n-2)


def partition_climbStairs(n: int) -> int:
    partitions = [1 for i in range(n)]
    index = 1
    solutions = 1
    last_index = n
    while index <= n//2:
        partitions[index-1] = 0
        partitions[index] = 2
        solutions += 1
        combination_index = index + 1
        while combination_index < last_index:
            temp = partitions[combination_index]
            partitions[combination_index] = partitions[combination_index-1]
            partitions[combination_index-1] = temp
            solutions += 1
            combination_index += 1
        last_index -= 1
        index += 1
    
    return solutions


'''
    partitions = [0 for i in range(n + 1)]
    solutions = []
    index = 1
    partitions[1] = n
    while index != 0:
        x = partitions[index - 1] + 1
        y = partitions[index] - 1
        print(x, y)
        index -= 1
        while x <= y:
            partitions[index] = x
            print(partitions)
            y -= x
            index += 1
        partitions[index] = x + y
        solutions.append(partitions[:index + 1])
    return len(solutions)
'''