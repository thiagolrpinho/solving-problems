'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

import pytest


# Definition for singly-linked list.
class ListNode:
     def __init__(self, x, next):
         self.val = x
         self.next = None


@pytest.mark.parametrize('input_and_output', [
    ([
        ListNode(1, ListNode(2, ListNode(3, None))),
        ListNode(4, ListNode(5, ListNode(6, None)))],
        [1, 2, 3, 4, 5, 6]),
    ])
def test_title_to_number(input_and_output):
    input_first_node = input_and_output[0][0]
    input_second_node = input_and_output[0][1]
    expected_output = input_and_output[1]
    predicted_output = mergeTwoLists(input_first_node, input_second_node)
    last_node = predicted_output
    while(last_node):
        assert last_node.val == expected_output[::-1].pop()
        last_node = last_node.next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    return ListNode(0, None)