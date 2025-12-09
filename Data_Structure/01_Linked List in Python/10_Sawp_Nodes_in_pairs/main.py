class Node:
    def __init__(my , val):
        my.data = val
        my.next = None

def swapNodeInPair(head):
    if head is None or head.next is None:
        return head
    
    first = head
    sec = head.next
    prev = None

    head = sec

    while first is not None and sec is not None:
        third = sec.next

        sec.next = first
        first.next = third

        if(prev is not None):
            prev.next = sec
        
        prev = first 
        first = third

        if(third != None):
            sec = third.next
        else:
            sec = None

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)


print("-" * 40)
print("Original list:")
temp = head
while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
print("-" * 40)


new_head = swapNodeInPair(head)


print("-" * 40)
print("Swapped list in pairs:")
temp = new_head
while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
print("-" * 40)
