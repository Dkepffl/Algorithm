def solution(a, b, c):
    arr = [a,b,c]
    if len(set(arr))==3:
        return sum(arr)
    elif len(set(arr))==2:
        return sum(arr)*sum([x**2 for x in arr])
    else:
        return sum(arr)*sum([x**2 for x in arr])*sum([x**3 for x in arr])

