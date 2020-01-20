'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10, -3, 0, 5, 9],

One possible answer is: [0, -3, 9, -10, null, 5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 '''

import pytest
from typing import List

@pytest.mark.parametrize('input_and_output', [
    ([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5]),
    ])
def test_sorted_array_to_bst(input_and_output):
    input_list = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = sortedArrayToBST(input_list)
    assert isinstance(predicted_output, TreeNode)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums: List[int]) -> TreeNode:
    return False