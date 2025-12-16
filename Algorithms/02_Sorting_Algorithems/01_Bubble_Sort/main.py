class BubbleSort: 
    def __init__(my, arr):
        my.arr = arr

    def sort(my):
        n = len(my.arr)
        for i in range(n):
            is_swapped = False
            for j in range(0, n-i-1):
                if my.arr[j] > my.arr[j+1]:
                    my.arr[j], my.arr[j+1] = my.arr[j+1], my.arr[j]
                    is_swapped = True

            # If no two elements were swapped by inner loop, then break
            if not is_swapped:
                break

        return my.arr
    
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSort(arr)
    sorted_arr = sorter.sort()
    print("Sorted array:", sorted_arr)

    arr1 = [5, 4, 3, 2, 1]
    sorter1 = BubbleSort(arr1)  
    sorted_arr1 = sorter1.sort()
    print("Sorted array:", sorted_arr1)