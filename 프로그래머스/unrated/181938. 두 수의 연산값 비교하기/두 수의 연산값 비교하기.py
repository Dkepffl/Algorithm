def solution(a, b):
    answer = 0
    ab = int(str(a)+str(b))
    a_b = 2*a*b
    if ab>=a_b:
        answer=ab
    else:
        answer=a_b
    return answer