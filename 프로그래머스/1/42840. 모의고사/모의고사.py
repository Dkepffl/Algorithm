def solution(answers):
    num_p = len(answers)
    s1 = ([1,2,3,4,5] * (num_p//5+1))[:num_p]
    s2 = ([2,1,2,3,2,4,2,5] * (num_p//8+1))[:num_p]
    s3 = ([3,3,1,1,2,2,4,4,5,5]*(num_p//10+1))[:num_p]
    
    for i in range(num_p):
        s1[i]=s1[i]-answers[i]
        s2[i]=s2[i]-answers[i]
        s3[i]=s3[i]-answers[i]
        
    g1 = sum([1 for i in range(num_p) if s1[i]==0])
    g2 = sum([1 for i in range(num_p) if s2[i]==0])
    g3 = sum([1 for i in range(num_p) if s3[i]==0])
    
    list_g = [g1,g2,g3]
    mg = max(g1,g2,g3)
    
    return [i+1 for i in range(3) if list_g[i]==mg]