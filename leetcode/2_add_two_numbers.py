'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

import pytest

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x, next):
         self.val = x
         self.next = next


@pytest.mark.parametrize('input_and_output', [
    ([
        ListNode(2, ListNode(4, ListNode(3, None))),
        ListNode(5, ListNode(6, ListNode(4, None)))],
        [7, 0, 8]),
    ([
        ListNode(5, None),
        ListNode(5, None)],
        [0, 1]),
    ([
        ListNode(0, None),
        ListNode(7, ListNode(3, None))],
        [7, 3])
    ])
def test_add_two_numbers(input_and_output):
    input_first_node = input_and_output[0][0]
    input_second_node = input_and_output[0][1]
    expected_output = input_and_output[1][::-1]
    predicted_output = addTwoNumbers(input_first_node, input_second_node)
    last_node = predicted_output
    assert isinstance(last_node, ListNode)
    while(last_node):
        print(last_node.val)
        expected_val = expected_output.pop()
        assert last_node.val == expected_val
        last_node = last_node.next
    assert len(expected_output) == 0


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    summation = residue = previous_last_node = 0
    first_node = l1
    while(l1 or l2):
        summation = 0
        if l1:
            summation += l1.val
        if l2:
            summation += l2.val
        summation += residue
        if l1:
            l1.val = summation % 10
            previous_last_node = l1
            l1 = l1.next
        else:
            previous_last_node.next = ListNode(summation % 10)
            previous_last_node = previous_last_node.next

        residue = int(summation/10)
        if l2:
            l2 = l2.next
    if residue:
        previous_last_node.next = ListNode(residue)
    return first_node
