# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        totallist = []
        for lst in lists:
            while lst:
                totallist.append(lst.val)
                lst = lst.next
        
        totallist.sort()
        
        head = ListNode(0)
        curr = head
        for val in totallist:
            curr.next = ListNode(val)
            curr = curr.next
        return head.next