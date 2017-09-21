# 9/14/2017
# Given a list, rotate the list to the right by k places, where k is non-negative.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0: return head
        
        len = 1
        temp = head
        
        while temp.next != None:
            temp = temp.next
            len += 1
        
        temp.next = head
        
        for i in range(1, len-k%len):
            head = head.next
        
        temp = head.next
        head.next = None
        
        return temp
