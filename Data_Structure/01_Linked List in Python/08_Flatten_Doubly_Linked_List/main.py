class Node:
    def __init__(my , val):
        my.data = val
        my.next = None
        my.prev = None
        my.child = None

class Solution:
    def __init__(self):
        pass

    def flatten(my , head):
        if head is None:
            return None
        
        curr = head

        while curr is not None:
            if curr.child is not None:
                newNext = curr.next
                curr.next = my.flatten(curr.child)

                if curr.next != None:
                    curr.next.prev = curr  #link child to curr

                curr.child = None

                tail = curr
                while tail and tail.next is not None:
                    tail = tail.next

                # Reconnect the saved next node
                if newNext is not None:
                    tail.next = newNext
                    newNext.prev = tail

            curr = curr.next
        
        return head
    
def main():
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    head.next = node2
    node2.prev = head
    node2.next = node3
    node3.prev = node2

    #Add a child list to node 2 (2 → child → 4 <-> 5)
    child1 = Node(4)
    child2 = Node(5)
    child1.next = child2
    child2.prev = child1
    node2.child = child1

    #Add a nested child list to node 5 (5 → child → 6)
    child3 = Node(6)
    child2.child = child3

    #Flatten the list
    s = Solution()
    flat = s.flatten(head)

    print("Flattened Doubly Linked List:")
    temp = flat
    while temp is not None:
        print(temp.data, end=" <-> " if temp.next else " -> None\n")
        temp = temp.next


if __name__ == "__main__":
    main()