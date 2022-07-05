import operator

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # v vsaki iteraciji dobimo najmanjsega in ga dodamo v array
        # potem povezemo, tako da je prav

        nodes = []
        for head in lists:
            while head is not None:
                nodes.append(head)
                head = head.next

        if len(nodes) == 0:
            return None

        nodes.sort(key=operator.attrgetter("val"))
        for i, node in enumerate(nodes):
            if i == len(nodes) - 1:
                node.next = None
            else:
                node.next = nodes[i + 1]
        return nodes[0]
