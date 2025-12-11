def next_greater_elements(arr , ans , s):
    for i in range(len(arr)-1 , -1 ,-1):
        while len(s) > 0 and s[-1] <= arr[i]:
            s.pop()

        if len(s) is 0:
            ans[i] = -1
        else:
            ans[i] = s[-1]

        s.append(arr[i])

    return ans 


arr = [6,8,0,1,3]
ans = [-1] * len(arr)
stack = []

ans = next_greater_elements(arr , ans , stack)
print("Next Greater Element for the given list is : ", ans)

