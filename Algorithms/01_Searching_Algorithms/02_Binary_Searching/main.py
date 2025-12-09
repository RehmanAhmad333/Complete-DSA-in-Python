class BinarySearch:
    def __init__(my , data):
        my.data = sorted(data)

    def search(my , target):
        low = 0
        high = len(my.data) - 1
        count = 0
        while low <= high :
            mid = low + (high - low ) // 2

            count +=1
            
            if my.data[mid] > target:
                high = mid -1
            elif my.data[mid] < target :
                low = mid + 1
            else:
                return mid , count

        return -1

arr = [15, 8, 23, 42, 4, 33]
print(sorted(arr))
obj = BinarySearch(arr)

search_ele = obj.search(23)
print(f"23 is at index : {search_ele[0]}  and it has {search_ele[1]} counts.\n" )
search_ele = obj.search(42)
print(f"42 is at index : {search_ele[0]}  and it has {search_ele[1]} counts.\n" )
search_ele = obj.search(99)
print(f"99 is not found {search_ele}")

