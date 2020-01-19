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
         self.next = next


@pytest.mark.parametrize('input_and_output', [
    ([
        ListNode(1, ListNode(2, ListNode(3, None))),
        ListNode(4, ListNode(5, ListNode(6, None)))],
        [1, 2, 3, 4, 5, 6]),
    ])
def test_title_to_number(input_and_output):
    input_first_node = input_and_output[0][0]
    input_second_node = input_and_output[0][1]
    expected_output = input_and_output[1][::-1]
    predicted_output = mergeTwoLists(input_first_node, input_second_node)
    last_node = predicted_output
    while(last_node):
        print(last_node.val)
        expected_val = expected_output.pop()
        assert last_node.val == expected_val
        last_node = last_node.next
    assert len(expected_output) == 0


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    
    if l2.val < l1.val:
        first_node = l2
        l2 = l2.next
    else:
        first_node = l1
        l1 = l1.next

    temp_node = first_node
    while(l1 and l2):
        if l2.val < l1.val:
            temp_node.next = l2
            temp_node = temp_node.next
            l2 = l2.next
        else:
            temp_node.next = l1
            temp_node = temp_node.next
            l1 = l1.next
    if l1 is not None:
        temp_node.next = l1
    elif l2 is not None:
        temp_node.next = l2
    return first_node
