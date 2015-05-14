# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head==None:
            return None
        self.pre = None
        self.curr = head
        self.next = head.next
        while self.curr.next != None:
            self.curr.next = self.pre
            self.pre = self.curr
            self.curr = self.next
            self.next = self.next.next
        self.curr.next = self.pre
        return self.curr
