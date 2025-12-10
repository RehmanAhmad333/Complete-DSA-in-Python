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
    
def is_valid_parentheses(s):
    a = Stack()
    for i in range(len(s)):
        if s[i] in "([{":
            a.push(s[i])
        else:
            if a.is_empty():
                return False 
            
            else:
                top = a.top()
                if (top == "(" and  s[i] == ")") or \
                    (top == "{" and s[i] == "}") or \
                    (top == "[" and s[i] == "]"):
                    a.pop()
                else:
                    return False
                
    if a.is_empty():
        return True
       
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("([{}])"))  # True
print(is_valid_parentheses("(]"))      # False
                
            
