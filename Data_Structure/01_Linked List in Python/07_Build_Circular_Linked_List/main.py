class Node:
    def __init__(my , val):
        my.data = val
        my.next = None
    
class CLL:
    def __init__(my):
        my.head = None
        my.tail = None

    def push_front(my , val):
        new_Node = Node(val)
        if my.head is None:
            my.head =my.tail= new_Node
            my.tail.next = my.head
            return
        
        new_Node.next = my.head
        my.head = new_Node
        my.tail.next = my.head

    def push_back(my , val):
        new_Node = Node(val)
        if my.head is None:
            my.head =my.tail= new_Node
            my.tail.next = my.head
            return 

        my.tail.next = new_Node
        my.tail = new_Node
        my.tail.next = my.head

    def pop_front(my):
        if my.head is None:
            print("Linked List is empty.")
            return 
        elif my.head == my.tail:
            my.head = my.tail = None
            return 
        else:
            temp = my.head
            my.head = my.head.next
            temp.next = None
            my.tail.next = my.head
            del temp
            return 

    def pop_back(my):
        if my.head is None:
            print("Linked List is empty.")
            return 
        elif my.head == my.tail:
            my.head = my.tail = None
            return 
        else:
            temp = my.head 
            while temp.next != my.tail:
                temp = temp.next

            my.tail = temp
            my.tail.next = my.head
         
    def display(my):
        if my.head is None:
                print("Linked List is empty.")
                return 
        print("-"*50)
        print("Elements of Circular Linked List  :  " , end="")
        print(my.head.data , " -> " , end="")
        temp = my.head.next
        while temp != my.head:
            print(temp.data , " -> ", end="")
            temp = temp.next

        print("(back to head)")
        print("-"*50)
        return
        
cll = CLL()
cll.push_back(10)
cll.push_back(20)
cll.push_front(5)
cll.push_front(50)
cll.push_back(40)
cll.push_back(30)
cll.display()
cll.pop_front()
cll.pop_back()
cll.display()
cll.pop_back()
cll.pop_front()
cll.display()
