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
from collections import deque

@pytest.mark.parametrize('input_and_output', [
    ([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5]),
    ([-10, -3, -1, 0, 5, 9], [0, -3, 9, -10, -1, 5])])
def test_sorted_array_to_bst(input_and_output):
    input_list = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = sortedArrayToBST(input_list)
    assert isinstance(predicted_output, TreeNode)
    node_stack = deque([predicted_output])
    i = 0
    while i < len(expected_output):
        print(i)
        current_node = node_stack.popleft()
        print(current_node)
        if current_node:
            assert current_node.val == expected_output[i]
            node_stack.append(current_node.left)
            node_stack.append(current_node.right)
        else:
            assert current_node == expected_output[i]
        i += 1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums: List[int]) -> TreeNode:
    if not nums:
        return None
    root_index = int(len(nums)/2)
    root = TreeNode(nums[root_index])
    list_stack = [(root, (0, root_index), (root_index+1, len(nums)))]
    while list_stack:
        current_node, lower_tuple, upper_tuple = list_stack.pop()
        if lower_tuple[0] < lower_tuple[1]:
            left_index = lower_tuple[0] + int((lower_tuple[1] - lower_tuple[0])/2)
            current_node.left = TreeNode(nums[left_index])
            list_stack.append((
                current_node.left,
                (lower_tuple[0], left_index),
                (left_index+1, lower_tuple[1])))
        if upper_tuple[0] < upper_tuple[1]:
            right_index = upper_tuple[0] + int((upper_tuple[1] - upper_tuple[0])/2)
            current_node.right = TreeNode(nums[right_index])
            list_stack.append((
                current_node.right,
                (upper_tuple[0], right_index),
                (right_index+1, upper_tuple[1])))
    return root


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
