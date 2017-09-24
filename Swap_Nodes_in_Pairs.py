# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        count
        if has next and is odd
        switch these two
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(None)
        pre.next = head
        dummy = pre
        count = 1
        
        while pre.next:
            if pre.val is None:
                pre = pre.next
                continue
            elif count%2 == 1:
                v1 = pre.val
                v2 = pre.next.val
                pre.val = v2
                pre.next.val = v1
            pre = pre.next
            count += 1
        return dummy.next
