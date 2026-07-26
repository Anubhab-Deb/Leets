# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lnew=ListNode(0)
        tail=lnew
        p1=l1
        p2=l2
        carry=0
        while p1 or p2 or carry:
            x=p1.val if p1 else 0
            y=p2.val if p2 else 0
            dsum=x+y+carry
            digit=dsum%10
            carry=dsum//10
            tail.next=ListNode(digit)
            tail=tail.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return lnew.next
        