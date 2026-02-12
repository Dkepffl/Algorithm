def solution(array):
    ## count 
    # index : 해당 숫자
    # value : 빈도
    count = [0] * (max(array)+1)
    
    for i in array:
        count[i] += 1
    
    m = 0 # 최빈값 개수
    f = max(count) 
    for c in count:
        if c == f:
            m += 1
            
    return -1 if m>1 else count.index(f)
        