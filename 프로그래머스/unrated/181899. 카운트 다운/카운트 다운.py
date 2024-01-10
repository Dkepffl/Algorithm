def solution(start, end_num):
    answer = []
    dif=start-end_num+1
    for i in range(0, dif):
        answer.append(start-i)
    return answer