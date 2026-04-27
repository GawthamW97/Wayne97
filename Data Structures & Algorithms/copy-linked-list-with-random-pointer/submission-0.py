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
        first = head
        seen = {None:None}
        while first:
            copyNode = Node(first.val)
            seen[first] = copyNode 
            first = first.next
        first = head
        while first:
            newNode = seen[first]
            newNode.next = seen[first.next]
            newNode.random = seen[first.random]
            first = first.next
        return seen[head]




