# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def traverseRecursive(node: ListNode, n: int) -> int:
    # zadnji node je prvi odzadaj
    if node.next is None:
        return 1

    node_index = traverseRecursive(node.next, n) + 1
    # pogledamo ali ja node.next tisti, ki ga moramo zbrisati
    if node_index - 1 == n:
        node.next = node.next.next

    return node_index


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ce je return val n pomeni, da brisemo prvega
        if traverseRecursive(head, n) == n:
            return head.next
        return head
