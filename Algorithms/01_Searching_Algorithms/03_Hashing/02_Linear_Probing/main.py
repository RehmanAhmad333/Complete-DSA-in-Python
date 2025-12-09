class LinearProbingHashTable:
    def __init__(my , size):
        my.size = size 
        my.table = [None] * my.size

    def hash_function(my , key):
        return key % my.size

    def insert(my ,  val , key:int):
        index = my.hash_function(key)
        org_index = index
        i = 0

        while my.table[index] is not None: # or my.table[index] != 0:
            sorted_key , sorted_value =  my.table[index]

            if sorted_key == key:
                my.table[index] = (key , val)
                print(f"Update key = {key} with value = {val} at index = {index}.\n")
                return 

            if my.table[index] == (0 , 0):
                my.table[index] = (key , val)
                print(f"Inserted key = {key} with value = {val} at index = {index}.")
                return
                
            i += 1
            index = (org_index + i) % my.size 
            
            if index == org_index:
                raise Exception("Hash Table is Full")
                return 

        my.table[index] = (key , val)
        print(f"Inserted key = {key} with value = {val} at index = {index}.")
        return

    def search(my , key:int):
            index = my.hash_function(key)
            org_index = index 
            i = 0

            while my.table[index] is not None:
                k , v = my.table[index]
                # print(k ,v)
                if key == k:
                    print(f"Found key = {key} with value = {v} at index = {index}")
                    return v

                i += 1
                index = (org_index + i) % my.size

                if index == org_index:
                    break

            print(f"Not found key = {key}.")
            return None
        
    def delete(my , key):
        index = my.hash_function(key)
        org_index = index 
        i = 0

        while my.table[index] is not None:
            k , v = my.table[index]
            if k == key:
                my.table[index] = (0 , 0)
                print(f"Delete key = {key} with value = {v} at index = {index}.")
                return 

            i+=1
            index = (org_index + i) % my.size  
            
            if index == org_index:
                break
                
        print(f"Not found key = {key}.")
        return 
        
    def display(my):
            print("-"*10 ,"Hash Table state" , "-"*10 )
            for i , item in enumerate(my.table):
                print(i , ":" , item)
        


ht = LinearProbingHashTable(10)

print("-"*10 , "Inserted Values" , "-"*10)
# Insert some keys
ht.insert("Ali" , 25)
ht.insert("Ahmad" , 35)
ht.insert("Huzafia" , 45 )
ht.insert("Yousaf" , 15)
ht.insert("Hammad" ,55)
ht.insert("Hammad" ,95)

ht.display()
print()
print()

print("-"*10 , "Search Values" , "-"*10)
ht.search(45)
ht.search(25)
ht.search(65)
print()
print()

print("-"*10 , "Deleted Values" , "-"*10)
ht.delete(35)
ht.delete(15)
ht.display()
print()
print()

print("-"*10 , "After Deleted Search Values" , "-"*10)
ht.search(45)
ht.search(95)
ht.display()
print()
print()


print("-"*10 , "After Deleted inserted Values" , "-"*10)
ht.insert("Naveed" , 13)
ht.insert("Hammad" ,42)
ht.insert("Hammad" ,15)
ht.display()
print()
print()

print("-"*10  ,"Today Task Complete Alhumallah" ,"-"*10 )