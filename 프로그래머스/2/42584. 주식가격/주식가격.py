def solution(prices):
    ans=[i for i in range(len(prices)-1,-1,-1)]
    stack=[0]
    for i in range(len(prices)):
        while stack and prices[stack[-1]]>prices[i]:
            j=stack.pop()
            ans[j]=i-j
        stack.append(i)
    return ans