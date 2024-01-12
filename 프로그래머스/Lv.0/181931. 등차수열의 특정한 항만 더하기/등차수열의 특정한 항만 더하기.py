def solution(a, d, included):
    answer = 0
    n=len(included)
    for i in range(0,n):
        if included[i]:
            answer += a+i*d
    return answer