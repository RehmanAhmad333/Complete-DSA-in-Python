def heapifyUp(arr , idx):
    perent_idx = (idx - 2) // 2
    if idx > 0 and arr[perent_idx] < arr[idx]:
        arr[perent_idx] , arr[idx] = arr[idx] , arr[perent_idx]
        heapifyUp(arr , perent_idx)

def heapifyDown(arr , idx):
    n = len(arr)
    largest_idx  =  idx

    left_child_idx = 2 * idx + 1
    right_child_idx = 2 * idx + 2

    if left_child_idx < n and arr[left_child_idx] > arr[largest_idx]:
        largest_idx = left_child_idx
    
    if right_child_idx < n and arr[right_child_idx] > arr[largest_idx]:
        largest_idx = right_child_idx

    if largest_idx != idx :
        arr[largest_idx] , arr[idx] = arr[idx] , arr[largest_idx]
        heapifyDown(arr , largest_idx)

def heapify(arr , idx , val):
    if arr[idx] > val:
        arr[idx] = val
        heapifyDown(arr, idx)
    else:
        arr[idx] = val
        heapifyUp(arr, idx)
    
    return arr


if __name__ == "__main__":
    arr = [20, 15, 18, 8, 10, 5, 14]
    print("Original array:", arr)
    print("Heapifying...\n")
    idx = 3
    val = 17
    updated_arr = heapify(arr, idx, val)
    print("Upated value at index", idx, "to", val)
    print("Updated array after heapify:", updated_arr)

    arr1 = [30, 25, 20, 15, 10, 5]
    idx1 = 2
    val1 = 35
    updated_arr1 = heapify(arr1, idx1, val1)
    print("\nUpated value at index", idx1, "to", val1)
    print("Updated array after heapify:", updated_arr1)