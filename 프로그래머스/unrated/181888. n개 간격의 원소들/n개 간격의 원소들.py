def solution(num_list, n):
    answer = []
    a=len(num_list)
    for i in range(0, a, n):
        answer.append(num_list[i])
    return answer


