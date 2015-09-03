#merge sort of linked list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        if not head or not head.next:
            return head
        else:
            mid = self.getMid(head)
            sHalf = mid.next
            mid.next = None
            return self.mergeSort(self.sortList(head),self.sortList(sHalf))
        
    def mergeSort(self, a, b):
        dummy = cur = ListNode(0)
        while a and b:
            if a.val <= b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        cur.next = a or b
        
        return dummy.next
        

        
    def getMid(self, head):
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
        
