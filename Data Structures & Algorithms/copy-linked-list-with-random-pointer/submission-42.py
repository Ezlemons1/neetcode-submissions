"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashlist = defaultdict(int)
        indexlist = {}
        counter = 0
        head2 = head
        while head:
            new = Node(head.val)
            indexlist[head] = counter
            hashlist[counter] = new
            counter += 1
            head = head.next
        hashlist[counter] = None
        indexlist[None] = counter

        counter2 = 0
        while head2:
            curr = hashlist[counter2]
            curr.next = hashlist[counter2 + 1]
            randindex = indexlist[head2.random]

            print(randindex)
            curr.random = hashlist[randindex]
            counter2 += 1
            head2 = head2.next
        

        return hashlist[0]
