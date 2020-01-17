'''Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3, 9, 20, null, null, 15, 7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
import pytest
from typing import List

@pytest.mark.parametrize('input_and_output', [
    ([3, 9, 20, None, None, 15, 7], 3)])
def test_palindrome_number(input_and_output):
    input_list_tree = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = max_depth(input_list_string)
    assert expected_output == predicted_output

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def max_depth(root: TreeNode) -> int:
    current_level = [root]
    greater_path = 0
    depth = 1
    while current_level and root:
        next_level = []
        depth += 1
        for next_node in current_level:
            if next_node:
                next_level.append(next_node)
            else:
                if greater_path < depth:
                    greater_path = depth
        current_level = next_level
    return greater_path
