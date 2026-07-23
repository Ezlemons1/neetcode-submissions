# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list1 = head
        list2 = slow
        prev = None
        while list2:
            l2next = list2.next
            list2.next = prev
            prev = list2
            list2 = l2next
        
        list2 = prev
        next1 = list1.next
        next2 = list2
        count = 0
        while next2 and next1:
            if count % 2 == 0:
                
                list1.next = next2
                
                next2 = next2.next
            elif count % 2 == 1:
                
                list1.next = next1
                next1 = next1.next
            count += 1
            list1 = list1.next
            print(list1.val)
        
        
            