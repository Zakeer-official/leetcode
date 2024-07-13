class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def linked_list_to_int(node: ListNode) -> int:
            num = 0
            mul = 1
            while node:
                num += node.val * mul
                mul *= 10
                node = node.next
            return num
        
        def int_to_linked_list(num: int) -> ListNode:
            if num == 0:
                return ListNode(0)
            prev_node = None
            head = None
            while num > 0:
                num, digit = divmod(num, 10)
                current_node = ListNode(digit)
                if head is None:
                    head = current_node
                else:
                    prev_node.next = current_node
                prev_node = current_node
            return head

        num1 = linked_list_to_int(l1)
        num2 = linked_list_to_int(l2)
        total = num1 + num2
        
        return int_to_linked_list(total)
