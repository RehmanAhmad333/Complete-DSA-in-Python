class Node:
    def __init__(my, val):
        my.data = val
        my.next = None


class Solution:
    def __init__(self):
        pass

    def middleOfLL(my, head):
        slow = head
        fast = head

        # Move fast by 2 and slow by 1
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # slow now points to middle node
        return slow


# MAIN FUNCTION 
head = Node(2)
head.next = Node(5)
head.next.next = Node(7)
head.next.next.next = Node(8)
head.next.next.next.next = Node(9)

s = Solution()
middle = s.middleOfLL(head)

print(f"Middle element of the Linked List is -> {middle.data}")
