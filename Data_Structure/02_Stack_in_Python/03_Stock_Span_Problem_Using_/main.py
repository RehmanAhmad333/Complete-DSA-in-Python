def stock_span(price):
    n = len(price)
    ans = [0] * n
    stack = []

    for i in range(n):
        while len(stack) > 0 and price[stack[-1]] <= price[i]:
            stack.pop()
        
        if len(stack) == 0:
            ans[i] = i + 1
        else:
            ans[i] = i - stack[-1]

        stack.append(i) 

    return ans

price = [100 , 80 , 60 , 70 , 60 , 75 , 85]
ans = stock_span(price)
print("Stock Span for the given price list is : ", ans)