# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):

        dummy = ListNode(0)
        dummy.next = head

        before = dummy

        for _ in range(left - 1):
            before = before.next


        current = before.next

        for _ in range(right - left):
            move = current.next
            current.next = move.next
            move.next = before.next
            before.next = move
        return dummy.next

