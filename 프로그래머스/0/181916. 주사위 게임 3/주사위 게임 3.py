def solution(a, b, c, d):
    n = len(set([a,b,c,d]))
    arr = [a,b,c,d]
    if n==1:
        return 1111*a
    elif n==4:
        return min(arr)
    elif n==3:
        temp=[]
        for i in arr:
            if arr.count(i)==1:
                temp.append(i)
        return temp[0]*temp[1]         
    elif n==2:
        p, q = set(arr)
        if arr.count(p)==3 and arr.count(q)==1:
            return (10*p+q)**2
        elif arr.count(p)==1 and arr.count(q)==3:
            return (10*q+p)**2
        else:
            return (p+q)*abs(p-q)
            