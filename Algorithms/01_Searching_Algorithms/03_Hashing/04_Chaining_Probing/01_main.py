class ChainingHashTable:
    def __init__(my , size):
        my.size = size
        my.table = [[] for _ in range(size)]

    def hash_fuction(my ,  key:int):
        return key % my.size
    
    def insert(my , key , value):
        idx = my.hash_fuction(key)

        for i , (k , v) in enumerate(my.table[idx]):
            if k == key :
                my.table[idx][i] = (key, value)
                print(f"Update key={key} with new value={value} at index={idx}")
                return
        
        my.table[idx].append((key , value))
        print(f"Insert key={key} with value={value} at index={idx}")
        return
    
    def search(my , key):
        idx = my.hash_fuction(key)
        
        for k, v in my.table[idx]:
            if k == key:
                print(f"Found key={key}, value={v} at index={idx}")
                return v 
            
        print(f"key={key} is not found in hash table.")
        return None
    
    def delete(my , key:int):
        idx = my.hash_fuction(key)
        bucket = my.table[idx]

        for i , (k ,v) in enumerate(my.table[idx]):
            if k == key:
                bucket.pop(i)
                print(f"Delete key={key} with value={v} at index={idx}")
                return
            
        print(f"key={key} is not found in hash table.")
        return 
    
    def display(my):
        for i , items in enumerate(my.table):
            print(i , " , " , items)

        return 
    
ht = ChainingHashTable(5)

ht.insert(10, "A")
ht.insert(15, "B")
ht.insert(20, "C")
ht.insert(7,  "D")
ht.insert(20, "H")

ht.display()

print("Search 15:", ht.search(15))
ht.delete(15)
ht.display()

 