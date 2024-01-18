def solution(intStrs, k, s, l):
    answer = []
    for number in intStrs:
        n = int(number[s:s+l])
        if n > k:
            answer.append(n)
    return answer