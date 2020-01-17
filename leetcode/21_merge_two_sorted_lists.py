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
    list_of_sorted_lists = [[], []]
    last_node = l1
    while last_node:
        list_of_sorted_lists[0].append(last_node.val)
        last_node = last_node.next
    
    last_node = l2
    while last_node:
        list_of_sorted_lists[1].append(last_node.val)
        last_node = last_node.next

    heap = []
    final_sorted_list = []
    heap = [
        (sublist[0], list_index, 0) 
        for list_index, sublist in enumerate(list_of_sorted_lists) if sublist]
    heapq.heapify(heap)
    # Here we have a heap with the first elements of each sublist
    while heap:
        # Now we have to pop the smaller element of the heap
        item, list_index, item_index = heapq.heappop(heap)

        final_sorted_list.append(item)
        # Then for each element we take we look for other inside that element initial sublist
        # Till they're over
        if item_index + 1 < len(list_of_sorted_lists[list_index]):
            next_tuple = (list_of_sorted_lists[list_index][item_index+1],
                            list_index, 
                            item_index+1)
            heapq.heappush(heap, next_tuple)

    last_node = None
    for val in final_sorted_list[::-1]:
        last_node = ListNode(val, last_node)

    return last_node