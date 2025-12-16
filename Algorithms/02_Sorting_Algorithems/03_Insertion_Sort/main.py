class InsertionSort:
    def __init__(my , arr):
        my.arr = arr

    def sort(my):
        n = len(my.arr)

        for i in range(1 , n):
            curr = my.arr[i]
            j= i-1

            while j >=0 and my.arr[j] > curr:
                my.arr[j+1] = my.arr[j]
                j -= 1

            my.arr[j+1] = curr
        
        return my.arr
    

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    sorter = InsertionSort(arr)
    sorted_arr = sorter.sort()
    print("Sorted array:", sorted_arr)

    arr1 = [5, 4, 3, 2, 1]
    sorter1 = InsertionSort(arr1)  
    sorted_arr1 = sorter1.sort()
    print("Sorted array:", sorted_arr1)