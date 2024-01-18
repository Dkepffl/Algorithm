def solution(my_string, queries):
    temp=list(my_string)
    for s,e in queries:
        temp[s:e+1]=list(reversed(temp[s:e+1]))
    return ''.join(temp)