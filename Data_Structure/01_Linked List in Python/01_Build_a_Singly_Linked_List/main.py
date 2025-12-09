class Node:
    def __init__(my, val):
        # Constructor to initialize a node with data and next pointer
        my.data = val
        my.next = None
        
# Define LinkedList class
class LinkedList:
    def __init__(self):
        # Initialize head and tail pointers
        self.head = None
        self.tail = None

    def push_front(my , val):
        # Insert a new node at the front of the list
        new_Node = Node(val)
        if my.head == None:
            my.head = my.tail = new_Node
            return
        else:
            new_Node.next = my.head
            my.head = new_Node
            return 

    def push_back(my , val):
        # Insert a new node at the end of the list
        new_Node = Node(val)
        if my.head == None:
            my.head = my.tail = new_Node
            return
        else:
            my.tail.next = new_Node
            my.tail = new_Node
            return 

    def pop_front(my):
        # Remove a node from the front of the list
        if my.head is None:
            print("The Linked List is empty!")
            return 
        else:
            temp = my.head
            my.head = my.head.next
            temp.next = None

        # If list becomes empty, reset tail as well
        if my.head == None:
            my.tail = None

    def pop_back(my):
        # Remove a node from the end of the list
        if my.head is None:
            print("The Linked List is empty!")
            return 
        elif my.head.next == None:   # if only one element
            my.head = my.tail = None
        else:
            temp = my.head
            while(temp.next != my.tail):
                temp = temp.next

            temp.next = None
            my.tail = temp
 
    def insert(my , pos , val):
        # Insert a new node at the given position
        if pos < 0:
            print("Invalid position!")
            return 
        if pos == 0:
            my.push_front(val)
            return 

        temp = my.head
        for i in range(0 , pos - 1):
            if temp is None:
                print("Invalid position!")
                return
            temp = temp.next

        new_Node = Node(val)

        new_Node.next = temp.next
        temp.next = new_Node
        return 

    def print_val(my):
        # Display all elements of the linked list
        if my.head == None:
            print("The Linked List is empty!")
            return
        temp = my.head
        print("Elements of Linked List : ", end="")
        while(temp is not None):
            print(temp.data , end=" -> ")
            temp = temp.next
        print("None")
        return 

    def search(my , val):
        # Search for a value in the linked list
        if my.head is None:
            print("The Linked List is empty!")
            return
        
        idx = 0
        temp = my.head
        while(temp is not None):
            if temp.data == val:
                return idx
            temp = temp.next
            idx += 1
        
        return -1   # return -1 if not found



ll = LinkedList()  # Create LinkedList object

print("\n--- Adding elements to Linked List ---")
ll.push_back(10)   # insert 10 at end
ll.push_back(20)   # insert 20 at end
ll.push_front(30)  # insert 30 at front
ll.push_back(40)   # insert 40 at end
ll.push_front(50)  # insert 50 at front
ll.print_val()     # output: 50 -> 30 -> 10 -> 20 -> 40 -> None

print("\n--- Removing elements ---")
ll.pop_back()      # remove from end (removes 40)
ll.pop_front()     # remove from front (removes 50)
ll.print_val()     # output: 30 -> 10 -> 20 -> None

print("\n--- Inserting at specific position ---")
ll.insert(1, 15)   # insert 15 after position 1
ll.print_val()     # output: 30 -> 15 -> 10 -> 20 -> None

print("\n--- Searching for element ---")
pos = ll.search(10)
if pos != -1:
    print(f"Element 10 found at position: {pos}")
else:
    print("Element not found!")

print("\n--- Final Linked List ---")
ll.print_val()
