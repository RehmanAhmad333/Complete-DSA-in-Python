class Node:
    def __init__(my ,val):
        my.data = val 
        my.next = None

class Solution:
    def __init__(my):
        pass

    def reverseList(my , head):
        curr = head
        new_next = None
        prev = None

        while curr is not None:
            new_next = curr.next
            curr.next = prev

            prev = curr
            curr = new_next

        return prev 

    def print_val(my , head):
        temp = head
        while temp is not None:
            print(temp.data , end = " ")
            temp = temp.next
        
        print()
        return 

head = Node(4)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(0)
            
s = Solution()

print("Linked List before reverse " , end= " : ")
s.print_val(head)

new_head = s.reverseList(head)

print("Linked List after reverse " , end= " : ")
s.print_val(new_head)