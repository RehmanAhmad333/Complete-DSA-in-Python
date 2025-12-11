class Solution(object):
    def nextGreaterElement(self, num1, num2):
        m = {}    
        s = []    #Stack
        ans = []

        for i in range(len(num2) -1 , -1 , -1):
            while len(s) > 0 and s[-1] <= num2[i]:
                s.pop()

            if len(s) == 0:
                m[num2[i]] = -1
            else:
                m[num2[i]] = s[-1]

            s.append(num2[i])
        
        for x in num1:
            ans.append(m[x])

        return ans
        
num1 = [4,1,2]
num2 = [1,3,4,2]

solution = Solution()
ans = solution.nextGreaterElement(num1 , num2)
print("Next Greater Element for the given list is : ", ans)