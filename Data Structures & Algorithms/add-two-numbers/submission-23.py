# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        new = ListNode
        ret = new
        while l1 or l2:
            if not l1:
                ans = l2.val + carry
                carry = 0
            elif not l2:
                ans = l1.val + carry
                carry = 0
            else:
                num1 = l1.val
                num2 = l2.val
                ans = num1 + num2 + carry
                carry = 0
            
            if ans >= 10:
                ans = ans % 10
                carry = 1

            curr = ListNode(ans)
            new.next = curr

            print("Carry: " + str(carry) + ", Ans: " + str(ans))
            
            new = new.next
            if not l1:
                l2 = l2.next
            elif not l2:
                l1 = l1.next
            else: 
                l1 = l1.next
                l2 = l2.next
            print(new.val)
        
        if carry != 0:
            print("true")
            new.next = ListNode(carry)
        
        return ret.next

