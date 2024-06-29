def solution(clothes):
    d_clothes = {j:1 for (i,j) in clothes}
    for (i,j) in clothes:
        d_clothes[j]+=1
    p=1
    for n in d_clothes.values():
        p*=n
    return p-1