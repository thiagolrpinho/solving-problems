'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''


import pytest

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


@pytest.mark.parametrize('input_and_output', [
    (([4,1,8,4,5], [5,0,1,8,4,5]), [8,4,5]),
    (([0,9,1,2,4], [3,2,4]), [2,4]),
    (([2,6,4], [1,5]), None),
    ])
def test_get_intersection_node(input_and_output):
    input_first_node = input_and_output[0][0]
    input_second_node = input_and_output[0][1]
    last_node = first_node = ListNode(input_first_node[0])
    for number in input_first_node[1:]:
        new_node = ListNode(number)
        last_node.next = new_node
        last_node = new_node
    
    last_node = second_node = ListNode(input_second_node[0])
    for number in input_second_node[1:]:
        new_node = ListNode(number)
        last_node.next = new_node
        last_node = new_node
    expected_output = input_and_output[1]
    
    predicted_output = getIntersectionNode(first_node, second_node)
    if not expected_output:
        assert not predicted_output
    else:
        last_node = predicted_output
        while(last_node):
            expected_val = expected_output.pop()
            assert last_node.val == expected_val
            last_node = last_node.next
        assert len(expected_output) == 0

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
        return None
    nodes_set = set()
    while headA:
        nodes_set.add(headA)
        headA = headA.next
    while headB:
        if headB in nodes_set:
            break
        headB = headB.next
    return headB