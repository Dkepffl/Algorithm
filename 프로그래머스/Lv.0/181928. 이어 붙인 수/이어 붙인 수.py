def solution(num_list):
    odd=''
    even=''
    for i in num_list:
        if i%2==0:
            odd=odd+str(i)
        else:
            even=even+str(i)
    return int(odd)+int(even)