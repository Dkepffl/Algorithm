def solution(my_string, overwrite_string, s):
    answer = list(my_string)
    end = s+len(overwrite_string)
    answer[s:end] = list(overwrite_string)
    answer = ''.join(answer)
    return answer