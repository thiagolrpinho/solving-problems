'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which
represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3, 2, 0, -4], pos = 1 Output: true Explanation: There is a cycle
in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1, 2], pos = 0 Output: true Explanation: There is a cycle in the
linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1 Output: false Explanation: There is no cycle in the
linked list.
'''

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


@pytest.mark.parametrize('input_and_output', [
    (([3, 2, 0, -4], 1), True),
    (([1, 2], 0), True),
    (([1], -1), False),
    ])
def test_has_cycle(input_and_output):
    input_first_node = input_and_output[0][0]
    cycle_position = input_and_output[0][1]
    expected_output = input_and_output[1]

    last_node = first_node = ListNode(input_first_node[0])
    count = 0
    cycle_node = None
    for number in input_first_node[1:]:
        new_node = ListNode(number)
        last_node.next = new_node
        if count == cycle_position:
            cycle_node = last_node
        count += 1
        last_node = new_node
    last_node.next = cycle_node

    predicted_output = hasCycle(first_node)
    assert expected_output == predicted_output


def hasCycle(head: ListNode) -> bool:
    ''' This solution is faster than using a set.
        Even though it's not as stable or intuitive '''
    slow_reference = fast_reference = head
    while (slow_reference and fast_reference and fast_reference.next):
        slow_reference = slow_reference.next
        fast_reference = fast_reference.next.next
        ''' Finds the last node in n/2 operations '''

        if slow_reference == fast_reference:
            ''' If slow reference is on an even index node
                and fast reference manages to reach it at the same time
                then it has a cycle.
            '''
            return True
    return False
