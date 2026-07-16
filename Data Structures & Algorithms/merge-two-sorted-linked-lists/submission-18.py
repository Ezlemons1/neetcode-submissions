# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        elif not list1 and not list2:
            return list1
        
        
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        ans = list1
        new1 = list1.next
        new2 = list2

        while new1 or new2:
            if not new1:
                list1.next = new2
                new2 = new2.next
            elif not new2:
                list1.next = new1
                new1 = new1.next

            elif new1.val <= new2.val:    # if list1 has the next smallest node
                list1.next = new1
                new1 = new1.next
            else:                       # if list2 has the next smallest node
                list1.next = new2
                new2 = new2.next
            list1 = list1.next

        return ans