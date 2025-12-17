class HeapSort:
    def __init__(my):
        pass

    def heapify(my , arr , n ,i):
        largest_idx  =  i

        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2

        if left_child_idx < n and arr[left_child_idx] > arr[largest_idx]:
            largest_idx = left_child_idx

        if right_child_idx < n and arr[right_child_idx] > arr[largest_idx]:
            largest_idx = right_child_idx

        if largest_idx != i :
            arr[largest_idx] , arr[i] = arr[i] , arr[largest_idx]
            my.heapify(arr , n , largest_idx)

    def sort(my , arr):
        n = len(arr)

        # Build a maxheap
        for i in range(n // 2 , -1 , -1):
            my.heapify(arr , n , i)

        # One by one extract elements from heap
        for end in range(n-1 , 0 , -1):
            arr[end] , arr[0] = arr[0] , arr[end]  # swap
            my.heapify(arr , end , 0)
        
        return arr
    
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    sorter = HeapSort()
    sorted_arr = sorter.sort(arr)
    print("Sorted array:", sorted_arr)

    arr1 = [64, 34, 25, 12, 22, 11, 90]
    sorter1 = HeapSort()  
    sorted_arr1 = sorter1.sort(arr1)
    print("Sorted array:", sorted_arr1)