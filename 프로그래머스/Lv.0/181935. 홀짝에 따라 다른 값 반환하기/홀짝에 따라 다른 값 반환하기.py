def solution(n):
    if n%2==0:
        answer=0
        for i in range(2,n+1,2):
            answer = answer+(i**2)
        return answer
    else :
        return sum(range(1,n+1,2))