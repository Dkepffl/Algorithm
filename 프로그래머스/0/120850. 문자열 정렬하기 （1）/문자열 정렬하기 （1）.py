def solution(my_string):
    answer=[]
    for x in my_string:
        if x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            answer.append(int(x))
    return sorted(answer)