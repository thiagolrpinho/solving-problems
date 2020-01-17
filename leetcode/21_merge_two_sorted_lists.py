'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

import pytest
import heapq

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
    heap = [
            (l1.val, 0, l1, l1.next),
            (l2.val, 1, l2, l2.next)]
    heapq.heapify(heap)
    last_current_node = None
    while heap:
        val, parity_disambiguity, current_node, old_next_node = heapq.heappop(heap)
        current_node.next = last_current_node
        last_current_node = current_node
        if old_next_node is not None:
            next_tuple = (
                            old_next_node.val,
                            parity_disambiguity,
                            old_next_node,
                            old_next_node.next)
            heapq.heappush(heap, next_tuple)

    prev = None
    current = last_current_node 
    while(current is not None):
        next = current.next
        current.next = prev 
        prev = current 
        current = next
    return prev
