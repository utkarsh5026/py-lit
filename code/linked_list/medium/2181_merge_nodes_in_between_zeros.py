from typing import Optional

class ListNode:
    def __init__(self, val: int=0, next: Optional["ListNode"]=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        sums = []
        curr = head
        while curr is not None:
            if curr.val == 0:
                if curr.next is None:
                    break
                
                between_sum = self.calc_sum(curr.next)
                sums.append(between_sum)

                while curr is not None and curr.next is not None and curr.next.val != 0:
                    curr = curr.next

            
            curr = curr.next

        return self.make_final_nodes(sums)
        


    def calc_sum(self, node: Optional[ListNode]):
        sum = 0
        while node is not None and node.val != 0:
            sum += node.val
            node = node.next

        return sum

    def make_final_nodes(self, nodes: list[int]):
        head = ListNode()
        curr = head

        for node in nodes:
            new_node = ListNode(node)
            curr.next = new_node
            curr = curr.next

        return head.next
