class Node:
    def __init__(my ,val):
        my.data = val
        my.next = None

class Solution:
    def mergeTwoLists(my ,head1 , head2):
        if head1 is None:
            return head2
        elif head2 is None:
            return head1
        
        if head1.data <= head2.data:
            head1.next = my.mergeTwoLists(head1.next , head2)
            return head1
        else:
            head2.next = my.mergeTwoLists(head1 , head2.next)
            return head2
        
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(5)
head1.next.next.next = Node(6)
head1.next.next.next.next = Node(10)

head2 = Node(1)
head2.next = Node(4)
head2.next.next = Node(5)
head2.next.next.next = Node(7)
head2.next.next.next.next = Node(11)
head2.next.next.next.next = Node(13)

s = Solution()

newHead = s.mergeTwoLists(head1 , head2)

temp = head1
print()
print("-" * 80)
print("List 1 elements : " , end=" ")
while temp is not None:
    print(temp.data , end=" , ")
    temp = temp.next
print("None")
print()
print("-" * 80)

temp = head2
print("\nList 2 elements : " , end=" ")
while temp is not None:
    print(temp.data , end=" , ")
    temp = temp.next
print("None")
print()
print("-" * 80)

temp = newHead
print("\nList elements after merge : " , end=" ")
while temp is not None:
    print(temp.data , end=" , ")
    temp = temp.next

print("None\n")
