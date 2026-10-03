# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            group_end = group_prev

            for _ in range(k):
                group_end = group_end.next

                if not group_end:
                    return dummy.next

            group_start = group_prev.next

            after_group = group_end.next

            prev = after_group
            current = group_start

            while current != after_group:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            group_prev.next = group_end

            group_prev = group_start
        