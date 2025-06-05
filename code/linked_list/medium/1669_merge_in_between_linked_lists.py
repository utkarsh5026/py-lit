from typing import Optional


class ListNode:
    def __init__(self, val: int=0, next: Optional["ListNode"]=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        if list1 is None:
            return list1
        
        merge_start = self.get_node_at_dist(list1, a - 1)
        if merge_start is None:
            return list1
        

        merge_end = self.get_node_at_dist(merge_start.next, b - a + 1)
        merge_start.next = list2

        while merge_start.next is not None:
            merge_start = merge_start.next

        merge_start.next = merge_end
        return list1

        

    def get_node_at_dist(self, head: Optional[ListNode], dist: int):
        while dist > 0 and head is not None:
            head = head.next
            dist -= 1
        return head
    


            
            
            

            
            