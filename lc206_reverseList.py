from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        # 遍历列表
        while head is not None:
            nextHead = head.next
            head.next = last
            last = head
            head = nextHead
        return last
