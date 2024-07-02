def solution(genres, plays):
    answer=[]
    gen_plays = {gen:0 for gen in set(genres)}
    for i in range(len(genres)):
        gen_plays[genres[i]]+=plays[i]
    
    p_g = dict(sorted(gen_plays.items(), key=lambda x:x[1],reverse=True)) 
    
    gen_sort={gen:[] for gen in p_g.keys()}
    for gen in p_g.keys():
        for j in range(len(genres)):
            if genres[j]==gen:
                gen_sort[gen].append([j, plays[j]])
                gen_sort[gen] = sorted(gen_sort[gen], key=lambda x:x[1],reverse=True)
    
    for gen in gen_sort.keys():
        for j in range(min(len(gen_sort[gen]),2)):
            answer.append(gen_sort[gen][j][0])
    return answer