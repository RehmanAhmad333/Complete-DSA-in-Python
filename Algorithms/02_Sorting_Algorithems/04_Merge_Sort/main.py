class MergeSort:
    def __init__(my):
        pass

    def merge(my , left , right):
        i = 0
        j = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i +=1
            else:
                merged.append(right[j])
                j +=1
            
        while i < len(left):
            merged.append(left[i])
            i +=1
        
        while j < len(right):
            merged.append(right[j])
            j +=1

        return merged
    
    def merge_sort(my , arr):
        if len(arr) <=1:
            return arr
        
        mid = len(arr) //2

        left_half = my.merge_sort(arr[:mid])
        right_half = my.merge_sort(arr[mid: ])

        return my.merge(left_half , right_half)
    

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorter = MergeSort()
    sorted_arr = sorter.merge_sort(arr)
    print("Sorted array:", sorted_arr)

    arr1 = [5, 4, 3, 2, 1]
    sorter1 = MergeSort()  
    sorted_arr1 = sorter1.merge_sort(arr1)
    print("Sorted array:", sorted_arr1)

    arr2 = [12, 11, 13, 5, 6]
    sorter2 = MergeSort()   
    sorted_arr2 = sorter2.merge_sort(arr2)
    print("Sorted array:", sorted_arr2)

    arr3 = [64, 34, 25, 12, 22, 11, 90]
    sorter3 = MergeSort()
    sorted_arr3 = sorter3.merge_sort(arr3)
    print("Sorted array:", sorted_arr3)
