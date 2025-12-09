class Node:
    def __init__(my , val):
        my.data = val      # stores node value
        my.next = None     # pointer to next node 


class Solution:
    def __init__(my):
        pass

    def deleteCycle(my , head):
        # if Linked List is empty, return None
        if(head == None):
            return None
        
        is_cycle = False   # flag to check if cycle exists
        slow = head        # slow pointer
        fast = head        # fast pointer

        # detect cycle using Floyd's cycle detection algorithm
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if(slow == fast):     # cycle detected
                is_cycle = True
                break

        # if no cycle found, return None
        if not is_cycle:
            print("No cycle found in the linked list.")
            return None
        
        # move slow pointer to head, keep fast where they met
        slow = head
        prev = None   # to keep track of node before fast pointer

        # move both one step until they meet at start of cycle
        while slow != fast :
            slow = slow.next
            prev = fast
            fast = fast.next

        # break the cycle
        prev.next = None
        print("Cycle deleted successfully.")
        return slow    # returns the starting node of the removed cycle
    


head = Node(2)
head.next = Node(5)
head.next.next = Node(7)
head.next.next.next = Node(8)
head.next.next.next.next = Node(9)

head.next.next.next.next.next = head.next.next   # creates a cycle (9 → 7)

s = Solution()

cycle_node = s.deleteCycle(head)

if cycle_node:
    print(f"Cycle started at node with value -> {cycle_node.data}")
else:
    print("No cycle found or deleted.")

print("\nLinked List after deleting cycle:")
temp = head
while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")



