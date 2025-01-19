# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            gcd_value = self.gcd(current.val, current.next.val)
            new_node = ListNode(gcd_value)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        return head

    @staticmethod
    def create_linked_list(lst):
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    @staticmethod
    def print_linked_list(head):
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# Test the function
head = Solution.create_linked_list([18, 6, 10, 3])
solution = Solution()
new_head = solution.insertGreatestCommonDivisors(head)
Solution.print_linked_list(new_head)