# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=0
        result=ListNode()
        mainresult=result
        while head:
            if head.val==0:
                result.next=ListNode(temp)
                result=result.next
                temp=0
            else:
                temp=temp+head.val
            head=head.next
        return mainresult.next.next
