class Node:
    def __init__(my , val):
        my.data = val
        my.next = None
        my.prev = None

class DLL:
    def __init__(my):
        my.head = None
        my.tail = None
    
    def push_front(my , val):
        new_Node = Node(val)
        if my.head is None:
            my.head = my.tail = new_Node
            return 
        
        new_Node.next = my.head
        my.head.prev = new_Node
        my.head = new_Node
        return
    
    def push_back(my , val):
        new_Node = Node(val)
        if my.head is None:
            my.head = my.tail = new_Node
            return
        else:
            my.tail.next = new_Node
            new_Node.prev = my.tail

            my.tail = new_Node
            return
        
    def pop_front(my):
        if my.head is None:
            print("Double Linked is empty ! Overflow.")
            return
        
        temp = my.head
        my.head = my.head.next
        if my.head is not None:
            my.head.prev = None

        temp.next = None
        del temp
        return 
    
    def pop_back(my):
        if my.head is None:
            print("Double Linked is empty ! Overflow.")
            return
        
        temp = my.tail
        my.tail=my.tail.prev

        if my.tail is not None:
            my.tail.next = None

        temp.prev = None
        del temp
        return 
    
    def display(my):
        if my.head is None:
            print("Double Linked is empty.")
            return

        temp = my.head
        print("Elements of Double Linked List : None <=> ",end="")
        while temp is not None:
            print(temp.data , end=" <=> ")
            temp = temp.next

        print("None")
        print("-" *40)
        return 
    
dll = DLL()
dll.push_back(30)
dll.push_front(20)
dll.push_back(40)
dll.push_front(10)

dll.push_back(60)
dll.push_front(40)
dll.push_back(80)
dll.push_front(20)

print("-" *40)
print("After pushing valuse \n ")
dll.display()

dll.pop_back()
dll.pop_front()
dll.pop_front()
dll.pop_back()

print("-" *40)
print("After poping valuse \n ")
dll.display()
