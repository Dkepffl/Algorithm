def solution(num_list):
    s=1
    for i in num_list:
        s=s*i
    s_2 = sum(num_list)**2
    return 1 if s<s_2 else 0