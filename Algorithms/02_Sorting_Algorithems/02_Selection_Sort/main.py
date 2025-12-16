class Selection_Sort:
    def __init__(my , arr):
        my.arr = arr

    def sort(my):
        n = len(my.arr)

        for i in range(n-1):
            min_idx = i
            for j in range(i+1 , n):
                if my.arr[j] < my.arr[min_idx]:
                    min_idx = j
                
            my.arr[i] , my.arr[min_idx] = my.arr[min_idx] , my.arr[i]

        return my.arr
    
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorter = Selection_Sort(arr)
    sorted_arr = sorter.sort()
    print("Sorted array:", sorted_arr)

    arr1 = [5, 4, 3, 2, 1]
    sorter1 = Selection_Sort(arr1)  
    sorted_arr1 = sorter1.sort()
    print("Sorted array:", sorted_arr1)
    