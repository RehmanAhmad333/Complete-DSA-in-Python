class Node:
    def __init__(my , key , value):
        my.key = key
        my.value = value
        my.next = None

class HashTableChaining:
    def __init__(my , size):
        my.size = size
        my.table = [None] * size

    def hash_function(my , key):
        total = 0
        for ch in key:
            total += ord(ch)
        return total % my.size

    def insert(my , key , value):
        idx = my.hash_function(key)
        new_Node = Node(key , value)

        new_Node.next = my.table[idx]
        
        my.table[idx] = new_Node
        print(f"Insert key = {key} with value = {value}  at index = {idx}.")
        return 

    def search(my , key):
        idx = my.hash_function(key)
        curr = my.table[idx]

        while curr is not None:
            if curr.key == key:
                print(f"Found key = {key} with value = {curr.value} at index = {idx}.")
                return True 
            curr = curr.next

        print(f"Not found key = {key} in hash table.")
        return None 

    def delete(my  , key):
        idx = my.hash_function(key)
        curr = my.table[idx]
        prev = None

        while curr is not None:
            if curr.key == key:
                if prev is None:
                    my.table[idx] = curr.next
                else:
                    prev.next = curr.next
                print(f"Delete key = {key} from index = {idx}.")
                return 

            prev = curr
            curr = curr.next

        print(f"key = {key} not found.")
        return 

    def display(my):
        for i in range (len(my.table)):
            curr = my.table[i]

            print(f"Elements at list {i}  : ",end="")
            while curr is not None:
                print(f"(key = {curr.key}  ,  value = {curr.value}) , ",end="")
                curr = curr.next

            print()
            i +=1



# Create a table of size 5
ht = HashTableChaining(5)

# Insert keys: "Ali", "Lia", "Azeem", "Omar", "Usman"

ht.insert("Ali" , 1111)    
ht.insert("Lia" , 1122)    
ht.insert("Azeem" , 2222)  
ht.insert("Omar" , 8325 )    
ht.insert("Usman" , 1427)

print()
ht.display()

# Search for "Ali", "Omar" and "XYZ" 

ht.search("Ali")
ht.search("Omar")
ht.search("XYZ")


# Delete "Lia"  

ht.delete("Lia")

ht.display()

