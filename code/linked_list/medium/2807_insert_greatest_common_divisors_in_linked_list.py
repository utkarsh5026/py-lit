from typing import Optional


class ListNode:
    def __init__(self, val: int=0, next: Optional["ListNode"]=None):
        self.val = val
        self.next = next

        
class Solution:
    def calc_gcd(self, a: int, b: int) -> int:
        """
        Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.
        
        Args:
            a (int): First number
            b (int): Second number
            
        Returns:
            int: Greatest Common Divisor of a and b
            
        Example:
            >>> gcd(48, 18)
            6
        """
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr is not None and curr.next is not None:
            a = curr.val
            b = curr.next.val

            gcd = ListNode(self.calc_gcd(a, b))
            curr_next = curr.next

            curr.next = gcd
            gcd.next = curr_next
            curr = curr_next

        return head
            


