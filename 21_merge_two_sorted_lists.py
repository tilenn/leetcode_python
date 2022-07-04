# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        nodesInOrder = []

        # se sprehodimo skozi oba lista
        # v nodesInOrder appendamo node z manjso vrednostjo
        while (list1 is not None) or (list2 is not None):
            # ce pridemo na konec pri enemu
            if list1 is None and list2 is not None:
                nodesInOrder.append(list2)
                list2 = list2.next
                continue
            if list2 is None and list1 is not None:
                nodesInOrder.append(list1)
                list1 = list1.next
                continue

            # preverimo kateri val je vecji
            # tistega dodamo in se pri njemu pomaknemo naprej
            if list1.val < list2.val:
                nodesInOrder.append(list1)
                list1 = list1.next
            else:
                nodesInOrder.append(list2)
                list2 = list2.next

        if len(nodesInOrder) == 0:
            return None

        for i, node in enumerate(nodesInOrder):
            if i + 1 == len(nodesInOrder):
                node.next = None
            else:
                node.next = nodesInOrder[i + 1]

        return nodesInOrder[0]
