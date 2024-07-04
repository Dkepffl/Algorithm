def solution(n):
    i = n+1
    p=bin(n)[2:].count('1')
    while True:
        if bin(i)[2:].count('1') == p:
            break
        i += 1
    return i