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

# function to find height of binary tree
def height(root):
    # base condition when binary tree is empty
    if root is None:
        return 0
    node_stack = [(1, root.left), (1, root.right)]
    max_height = 1
    while node_stack:
        height, next_node = node_stack.pop()
        while next_node:
            height += 1
            if height > max_height:
                max_height = height
            node_stack.append((height, next_node.right))
            next_node = next_node.left

    return max_height


# function to check if tree is height-balanced or not
def isBalanced(root):

    # Base condition
    if root is None:
        return True

    # for left and right subtree height
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) > 1:
        return False

    node_stack = [(root.left), (root.right)]
    while node_stack:
        next_node = node_stack.pop()
        while next_node:
            left_height = height(next_node.left)
            right_height = height(next_node.right)
            if abs(left_height - right_height) > 1:
                return False
            node_stack.append(next_node.right)
            next_node = next_node.left
    return True

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.right.left = TreeNode(6) 
root.left.left.left = TreeNode(7)


print(isBalanced(root))

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.left.left.left = TreeNode(8) 

print(isBalanced(root))