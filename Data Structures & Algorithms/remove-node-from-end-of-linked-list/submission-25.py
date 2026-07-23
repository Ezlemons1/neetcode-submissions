# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = head
        first, second = head, head
        prev = head
        
        for i in range(n):
            second = second.next
        
        while second:
            prev = first
            first = first.next
            second = second.next
        
        if prev == first:
            ans = ans.next
        else:
            prev.next = first.next

        return ans

