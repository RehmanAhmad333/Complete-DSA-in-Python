class Node:
    def __init__(my , val):
        my.data = val
        my.next = None  

class Solution:
    def reverseKGroup(my ,head , k):
        temp = head
        cunt = 0

        while cunt < k:
            if temp is None:
                return head
            temp = temp.next
            cunt +=1

        preNode = my.reverseKGroup(temp , k)

        temp = head
        cunt = 0

        while cunt < k:
            new_Next = temp.next 
            temp.next = preNode

            preNode = temp
            temp = new_Next

            cunt +=1

        return preNode #return as a new head

def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original list:")
    printList(head)

    k = 2  # Reverse in groups of 2
    s = Solution()
    new_head = s.reverseKGroup(head, k)

    print(f"\nReversed in groups of {k}:")
    printList(new_head)



if __name__ == "__main__":
    main()