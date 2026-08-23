# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        last = head
        begin = True
        if k == 1:
            return head

        while start:
            ### check if there are at least k nodes remaining
            dummy = start
            temp = start
            count = 0
            while dummy.next and count < k-1:
                dummy = dummy.next
                count += 1
            if count < k-1:
                print("triggered")
                last.next = start
                break
            ###
            
            prev = None
            for i in range(k):
                nxt = start.next
                start.next = prev
                prev = start
                start = nxt
            head.next = start
            head = head.next
            if begin:
                curr = prev
                begin = False
            else:
                last.next = prev
                last = temp

            # start is in correct position here, need prev to point to node behind start

        return curr
    
        



# first iterate k times, reverse list of k length
# then, from head node, traverse k times
# repeat reversal from there as if start of new linkedlist
