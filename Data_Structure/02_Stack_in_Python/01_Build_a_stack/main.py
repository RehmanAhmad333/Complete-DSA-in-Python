class Stack:
    def __init__(my):
        my.items = []
    
    def is_empty(my):
        return len(my.items) == 0
    
    def push(my, item):
        my.items.append(item)
    
    def pop(my):
        if my.is_empty():
            raise IndexError("pop from empty stack")
        return my.items.pop()
    
    def top(my):
        if my.is_empty():
            raise IndexError("peek from empty stack")
        return my.items[-1]
    

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print(stack.top())  # Output: 3
    print(stack.pop())  # Output: 3
    print(stack.is_empty())  # Output: False
    print(stack.pop())  # Output: 2
    print(stack.pop())  # Output: 1
    print(stack.is_empty())  # Output: True