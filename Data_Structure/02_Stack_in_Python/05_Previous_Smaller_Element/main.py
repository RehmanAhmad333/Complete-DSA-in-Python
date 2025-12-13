def prev_smaller_element(arr):
    ans = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while len(stack) >0 and stack[-1] >= arr[i]:
            stack.pop()

        if len(stack) == 0:
            ans[i] = -1
        else:
            ans[i] = stack[-1]

        stack.append(arr[i])

    return ans 

if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    result = prev_smaller_element(arr)
    print("Previous Smaller Elements:", result)

    arr1 = [3, 2, 1]
    result1 = prev_smaller_element(arr1)
    print("Previous Smaller Elements:", result1)

    arr2 = [1, 2, 3 , 4 , 5 ,0 , 4 , 7 , 1]
    result2 = prev_smaller_element(arr2)
    print("Previous Smaller Elements:", result2)