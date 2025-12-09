class HashTable:
    def __init__(my , size):
        my.size = size
        my.table = [None] * size

    def hash_function(my , key):
        return key % my.size
    
    def insert(my , key , value):
        idx = my.hash_function(key)
        my.table[idx] = value

        print(f"\nInserted key: {key} , value : {value} at index: {idx}")
        return
    
    def delete(my , key):
        idx = my.hash_function(key)
        my.table[idx] = None

        print(f"\nDeleted key: {key} at index: {idx}")
        return

    def search(my , key):
        idx = my.hash_function(key)
        value = my.table[idx]

        if value is not None:
            print(f"\nFound key: {key} , value : {value} at index: {idx}")
        else:
            print(f"\nKey: {key} not found in hash table.")
        
        return value
    
    def display(my):
        print("\nHash Table contents:")
        for idx , value in enumerate(my.table):
            print(f"Index {idx} : {value}")
        
        print()
        return
    
ht = HashTable(10)
ht.insert(1 , "One")
ht.insert(12 , "Twelve")
ht.insert(24 , "Twenty Four")

ht.delete(12)

ht.insert(3 , "Three")
ht.insert(5 , "Five")


ht.search(2)

ht.display()
print("Hashing module executed successfully.")