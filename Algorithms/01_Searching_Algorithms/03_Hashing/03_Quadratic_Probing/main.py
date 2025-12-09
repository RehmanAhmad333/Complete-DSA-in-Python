class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key: int) -> int:
        return key % self.size

    def insert(self, key: int, value):
        base_index = self.hash_function(key)
        i = 0

        while True:
            index = (base_index + i * i) % self.size

            if self.table[index] is None:
                self.table[index] = (key, value)
                print(f"Inserted key={key}, value={value} at index={index}")
                return
            
            i += 1
            if i == self.size:
                print("Table is full, cannot insert")
                return

    def search(self, key: int):
        base_index = self.hash_function(key)
        i = 0

        while i < self.size:
            index = (base_index + i * i) % self.size

            if self.table[index] is None:
                print(f"Key={key} not found in hash table.")
                return None  # key not found
            
            k, v = self.table[index]
            if k == key:
                print(f"Found key={key}, value={v} at index={index}")
                return v
            
            i += 1
        
        print(f"Key={key} not found in hash table.")
        return None

    def display(my):
        print("\nHash Table Contents:")
        for i, entry in enumerate(my.table):
            if entry is None:
                print(f"Index {i}: Empty")
            else:
                print(f"Index {i}: Key={entry[0]}, Value={entry[1]}")
        print()

    
ht = QuadraticProbingHashTable(10)
ht.insert(1 , "One")    
ht.insert(12 , "Twelve")
ht.insert(24 , "Twenty Four")
ht.insert(3 , "Three")
ht.insert(13 , "Thirteen")
ht.insert(22 , "Twenty Two")
ht.insert(33 , "Thirty Three")

ht.search(24)
ht.search(5)

ht.display()
print("End of Program\n")