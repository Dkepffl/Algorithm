def solution(numbers):
    num = sorted([str(i) for i in numbers], key=lambda x:x*3,reverse=True)
    return str(int(''.join(num)))