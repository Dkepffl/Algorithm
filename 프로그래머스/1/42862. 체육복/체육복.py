def solution(n, lost, reserve):
    los =list(set(lost)-set(reserve))
    res = list(set(reserve)-set(lost))
    
    for i in los:
        if i-1 in res:
            res.remove(i-1)
        elif i+1 in res:
            res.remove(i+1)
        else : n-=1
    return n