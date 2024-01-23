def solution(arr, queries):
    for s,e in queries:
        arr[s:e+1]=[i+1 for i in arr[s:e+1]]
    return arr