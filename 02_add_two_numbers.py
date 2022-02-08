from re import L
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# l1, l2 in return type so ListNode
def addTwoNumbers(l1, l2):
    l = ListNode()
    iter = l
    overflow = 0

    while l1 or l2 or overflow:
        if iter.next is None:
            iter.next = ListNode()
            iter = iter.next
        sum = overflow
        if l1:
            sum += l1.val
            l1 = l1.next

        if l2:
            sum += l2.val
            l2 = l2.next

        overflow = sum // 10
        sum = sum % 10
        iter.val = sum
    return l.next


def create_number(list):
    l = ListNode()
    iter = l

    # detektiramo ali je stevilo zadnje v seznamu
    list_len = len(list)

    for i, num in enumerate(list):
        iter.val = num
        if i != list_len - 1:
            iter.next = ListNode()
        iter = iter.next

    return l


def printLinkedList(l):
    while l is not None:
        print(l.val)
        l = l.next


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

x = addTwoNumbers(create_number(l1), create_number(l2))
# printLinkedList(create_number(l1))
# printLinkedList(create_number(l2))
printLinkedList(x)
