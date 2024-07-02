def solution(s):
    b=0
    for i in range(len(s)):
        if s[i]=='(': b-=1
        elif s[i]==')':b+=1
        
        if b>0:return False
    if b!=0:return False
    return True