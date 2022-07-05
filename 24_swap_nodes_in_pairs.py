# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def swap(head):
    if head is None or head.next is None:
        return head
    tmp = head.next
    head.next = tmp.next
    tmp.next = head
    return tmp


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        i = 0
        while tmp is not None:
            if i == 0:
                tmp = swap(tmp)
                head = tmp
                i += 1
                continue

            # se pomaknemo za eno naprej
            if tmp.next is not None:
                tmp = tmp.next
                tmp.next = swap(tmp.next)
                tmp = tmp.next
            else:
                break

        return head
