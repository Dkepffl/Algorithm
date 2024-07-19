def solution(n):
    i=1
    answer=0
    while i**2 <= n:
        if n%i==0:
             answer+=1
        i+=1
    if (i-1)**2 == n:
        return 2*answer-1
    return 2*answer