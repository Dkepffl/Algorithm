def solution(participant, completion):
    part = {p : 0 for p in participant}
    for people in participant:
        part[people] +=1
    for co in completion:
        if co in part.keys():
            part[co]-=1
    for p in part.keys():
        if part[p] > 0:
            return p